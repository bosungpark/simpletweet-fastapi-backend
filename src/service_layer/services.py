from sqlalchemy import text, bindparam

from src.adapters.cache import redis_repository
from src.adapters.repository import tweet_repository, follow_repository
from src.domain.models import Tweet


def publish_timeline(user_id: int):
    tweet= Tweet(sender_id=user_id)
    # persist in rdbm
    tweet_repository.add(tweet)
    tweet_repository.commit()
    # cache in redis
    redis_repository.add(user_id, tweet.id)
    redis_repository.commit()
    # get follower ids
    follows = follow_repository.list('follower_id', user_id)
    followee_ids = [follow.followee_id for follow in follows]
    # publish message
    redis_repository.publish(message={'followee_ids':followee_ids, 'timeline_id':tweet.id})


def subscribe_timeline_using_rdbm(user_id):
    tweets = tweet_repository._session.execute(  # noqa
            text("""  
            SELECT tweets.* FROM tweets
            JOIN users ON tweets.sender_id = users.id
            JOIN follows ON follows.followee_id = users.id
            WHERE follows.follower_id = :user_id
            """).bindparams(bindparam('user_id', expanding=True)),
            params={'user_id': user_id}
        ).all()
    return tweets


def subscribe_timeline_using_redis(user_id):
    tweets = redis_repository.list(user_id=user_id)
    return tweets
