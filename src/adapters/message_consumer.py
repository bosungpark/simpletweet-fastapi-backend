import json

from src.main import redis_instance


def redis_message_consumer():
    pubsub = redis_instance.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("publish_message")
    for m in pubsub.listen():
        message: dict = json.loads(m)

        follower_ids = message.get("follower_ids", [])
        timeline_id = message.get("timeline_id", "")
        for follower_id in follower_ids:
            redis_instance.lpush(f"{follower_id}", timeline_id)


if __name__ == "__main__":
    redis_message_consumer()
