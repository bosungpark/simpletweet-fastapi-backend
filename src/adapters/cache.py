from collections import defaultdict, deque


class InMemoryCache(object):
    _followers = defaultdict(list)  # 팔로워 테이블, {user_id: [follower_id]}
    _timelines = defaultdict(deque)  # 타임라인 테이블, {follower_id: deque(timeline)}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(InMemoryCache, cls).__new__(cls)
        return cls._instance  # type: ignore

    def publish_timeline(self, user_id, timeline):
        followers = self._followers[user_id]
        for follower_id in followers:
            self._timelines[follower_id].appendleft(timeline)

    def subscribe_timeline(self, user_id):
        return self._timelines[user_id]


in_memory_cache = InMemoryCache()
