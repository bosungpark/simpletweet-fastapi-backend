from src.domain.models import User, Follow, Tweet


def create_dummy_users(session, number:int):
    users = []
    for _ in range(number):
        user = User(screen_name="whatever")
        session.add(user)
        users.append(user)
    session.commit()
    return users


def create_dummy_follow(session, follower_id, followee_id):
    follow = Follow(
        follower_id=follower_id,
        followee_id=followee_id
    )
    session.add(follow)
    session.commit()


def create_dummy_tweet(session, redis_instance, sender_id):
    tweet = Tweet(
        sender_id=sender_id
    )
    session.add(tweet)
    session.commit()
    redis_instance.sadd(sender_id, tweet.id)


def create_dummy_relationship(session, redis_instance):
    [follower] = create_dummy_users(session, number=1)
    followees = create_dummy_users(session, number=100)

    for followee in followees:
        create_dummy_follow(session, follower_id=follower.id, followee_id=followee.id)
        create_dummy_tweet(session, redis_instance, sender_id=followee.id)
