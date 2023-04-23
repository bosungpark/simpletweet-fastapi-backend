from src.adapters.orm import session
from src.domain.models import Tweet


def publish_timeline(user_id):
    tweet= Tweet(sender_id=user_id)
    session.add(tweet)
    session.commit()


def subscribe_timeline(user_id):
    timelines = session.query(Tweet).filter(Tweet.sender_id==user_id).all()
    return timelines
