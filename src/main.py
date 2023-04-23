import json
import time

import redis
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.adapters.orm import metadata, start_mappers

# sqlite
engine = create_engine("sqlite+pysqlite:///:memory:", connect_args={"check_same_thread": False}, future=True)
metadata.create_all(engine)
conn = engine.connect()
start_mappers()
sqlalchemy_session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))

# redis
redis_instance: redis.Redis = redis.StrictRedis(host="127.0.0.1", port="6379", db=0, decode_responses=True) # type: ignore

pubsub = redis_instance.pubsub(ignore_subscribe_messages=True)
while True:
    pubsub.subscribe("publish_message")
    for m in pubsub.listen():
        message: dict = json.loads(m)

        follower_ids = message.get("follower_ids", [])
        timeline_id = message.get("timeline_id", "")
        for follower_id in follower_ids:
            redis_instance.lpush(f"{follower_id}", timeline_id)
    time.sleep(1)