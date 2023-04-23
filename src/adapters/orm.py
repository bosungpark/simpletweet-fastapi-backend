from sqlalchemy import MetaData, Table, Column, Integer, String, create_engine
from sqlalchemy.orm import mapper, scoped_session, sessionmaker

from src.domain import models

metadata=MetaData()

tweets =Table(
    "tweets",metadata,
    Column("id",Integer, primary_key=True, autoincrement=True),
    Column("sender_id",Integer),
)

user=Table(
    "user",metadata,
    Column("id",Integer, primary_key=True, autoincrement=True),
    Column("screen_name",String(250)),  # whatever
    Column("follow_id",Integer),  # follow table id
)

follows=Table(
    "follows",metadata,
    Column("id",Integer, primary_key=True, autoincrement=True),
    Column("follower_id",Integer, primary_key=True, autoincrement=True),
    Column("followee_id",Integer),
)


def start_mappers():
    tweets_mapper= mapper(models.Tweet, tweets)
    follow_mapper = mapper(models.Follow, follows)
    user_mapper= mapper(models.User,user)


engine = create_engine("sqlite+pysqlite:///:memory:", connect_args={"check_same_thread": False}, future=True)
metadata.create_all(engine)
conn = engine.connect()
start_mappers()
session = scoped_session(sessionmaker(bind=engine, expire_on_commit=False))
