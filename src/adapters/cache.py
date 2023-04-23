import redis

redis_instance: redis.Redis = redis.StrictRedis(host="127.0.0.1", port="6379", db=0, decode_responses=True)


class RedisRepository:
    _tracked = dict()

    def __init__(self):
        self.redis = redis_instance

    def add(self, key, value):
        self._tracked[key] = value

    def commit(self):
        for key, value in self._tracked.items():
            self.redis.set(key, value)
        self._tracked.clear()

    def get(self, key):
        return self.redis.get(str(key))

    def rollback(self):
        self._tracked.clear()

    def set_timeline_id(self, user_id, timeline_id):
        self.redis.lpush(f"{user_id}", timeline_id)

    def get_timeline_ids(self, user_id):
        return self.redis.get(f"{user_id}")
