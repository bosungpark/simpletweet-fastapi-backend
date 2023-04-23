import redis

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from src.adapters.orm import metadata, start_mappers

# fastapi
from src.dummy import create_dummy_relationship

...

# sqlite
engine = create_engine("sqlite+pysqlite:///:memory:", connect_args={"check_same_thread": False}, future=True)
metadata.create_all(engine)
connection = engine.connect()
connection.begin()
start_mappers()
sqlalchemy_session = scoped_session(sessionmaker(bind=connection, expire_on_commit=False))

# redis
redis_instance: redis.Redis = redis.StrictRedis(host="127.0.0.1", port="6379", db=0, decode_responses=True) # type: ignore

# dummy data
create_dummy_relationship(sqlalchemy_session)
