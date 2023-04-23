from src.domain.models import User, Follow


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


def create_dummy_relationship(session):
    [follower] = create_dummy_users(session, number=1)
    followees = create_dummy_users(session, number=100)

    for followee in followees:
        create_dummy_follow(session, follower_id=follower.id, followee_id=followee.id)
