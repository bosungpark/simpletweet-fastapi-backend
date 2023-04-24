import json

from src.domain.models import User, Follow, Tweet


def create_dummy_users(session, number:int):
    users = []
    for i in range(number):
        user = User(screen_name=f"whatever{i}")
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


def create_dummy_relationship(session, redis_instance):
    [follower] = create_dummy_users(session, number=1)
    followees = create_dummy_users(session, number=100)

    # map relation
    for followee in followees:
        create_dummy_follow(session, follower_id=follower.id, followee_id=followee.id)

        tweet = Tweet(sender_id=followee.id)
        # persist in rdbm
        session.add(tweet)
        session.commit()
        # get follower ids
        followee_ids = [followee.id for followee in followees]
        # publish message
        redis_instance.publish(channel="publish_message", message=json.dumps({'followee_ids': followee_ids, 'timeline_id': tweet.id}))



