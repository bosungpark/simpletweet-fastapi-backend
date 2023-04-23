from sqlalchemy import text, bindparam

from src.adapters.cache import redis_repository
from src.adapters.repository import tweet_repository, user_repository
from src.domain.models import Tweet, User, Follow


def publish_timeline(user_id: int):
    tweet= Tweet(sender_id=user_id)
    # persist in rdbm
    tweet_repository.add(tweet)
    tweet_repository.commit()
    # cache in redis
    redis_repository.add(user_id, tweet.id)
    redis_repository.commit()
    # get follower ids
    users = user_repository._session.query(User)\
        .join(Follow, Follow.follower_id == User.id)\
        .filter(User.id == user_id).all()
    follower_ids = [user.follower_id for user in users]
    # publish message
    redis_repository.publish(message={'follower_ids':follower_ids, 'timeline_id':tweet.id})


def subscribe_timeline_using_rdbm(user_id):
    tweets = tweet_repository._session.execute(  # noqa
            text("""  
            SELECT tweets.*, users.* FROM tweets
            JOIN users ON tweets.sender_id = users.id
            JOIN follows ON follows.followee_id = users.id
            WHERE follows.follower_id = :user_id
            """).bindparams(bindparam('user_id', expanding=True)),
            params={'user_id': user_id}
        )
    return tweets


def subscribe_timeline_using_redis(user_id):
    tweets = redis_repository
    return tweets
