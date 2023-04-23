import json
import logging

from src.main import redis_instance

logger = logging.getLogger(__name__)


class RedisRepository:
    _tracked = dict()

    def __init__(self, redis_instance):
        self.redis = redis_instance

    def add(self, key, value):
        self._tracked[key] = value

    def commit(self):
        for key, value in self._tracked.items():
            self.redis.lpush(f"{key}", str(value))
        self._tracked.clear()

    def list(self, user_id):
        return self.redis.get(f"{user_id}") or []

    def rollback(self):
        self._tracked.clear()

    def publish(self, message: dict, channel="publish_message"):
        logging.error(f"Publishing: channel={channel}, message={message}!")
        self.redis.publish(channel, json.dumps(message))


redis_repository = RedisRepository(redis_instance=redis_instance)
