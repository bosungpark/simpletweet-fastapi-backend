import logging

from src.main import redis_instance

logger = logging.getLogger(__name__)


def redis_message_consumer():
    pubsub = redis_instance.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe("publish_message")
    for message in pubsub.listen():
        logging.error(f"Subscribing: message={message}!")
        followee_ids = message.get("followee_ids", [])
        timeline_id = message.get("timeline_id", "")
        for followee_id in followee_ids:
            redis_instance.lpush(f"{followee_id}", timeline_id)


if __name__ == "__main__":
    redis_message_consumer()
