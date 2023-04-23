from src.adapters.repository import tweet_repository
from src.domain.models import Tweet


def publish_timeline(user_id: int):
    tweet= Tweet(sender_id=user_id)
    tweet_repository.add(tweet)
    tweet_repository.commit()


def subscribe_timeline(user_id):
    tweets = tweet_repository._session.execute(
            f"SELECT tweets.*, users.* FROM tweets "  # type: ignore
            f"JOIN users ON tweets.sender_id = users.id) "  
            f"JOIN follows ON follows.followee_id = users.id "
            f"WHERE follows.follower_id = {user_id}"
        )
    return tweets
