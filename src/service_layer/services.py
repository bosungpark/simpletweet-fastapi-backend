from src.adapters.orm import session
from src.adapters.repository import tweet_repository
from src.domain.models import Tweet


def publish_timeline(user_id: int):
    tweet= Tweet(sender_id=user_id)
    session.add(tweet)
    session.commit()


def subscribe_timeline(user_id):
    timelines = tweet_repository.list(column="user_id", value=user_id)
    return timelines
