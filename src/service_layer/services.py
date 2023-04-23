from sqlalchemy import text, bindparam

from src.adapters.repository import tweet_repository
from src.domain.models import Tweet


def publish_timeline(user_id: int):
    tweet= Tweet(sender_id=user_id)
    tweet_repository.add(tweet)
    tweet_repository.commit()


def subscribe_timeline(user_id):
    tweets = tweet_repository._session.execute(
            text("""  
            SELECT tweets.*, users.* FROM tweets
            JOIN users ON tweets.sender_id = users.id) 
            JOIN follows ON follows.followee_id = users.id
            WHERE follows.follower_id = :user_id
            """).bindparams(bindparam('user_id')),
            params={'user_id':user_id}
        )
    return tweets
