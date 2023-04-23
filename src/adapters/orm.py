from sqlalchemy import MetaData, Table, Column, Integer, String, BigInteger
from sqlalchemy.orm import registry

from src.domain import models

metadata=MetaData()
mapper_registry = registry(metadata=metadata)

tweets =Table(
    "tweets",metadata,
    Column("id", BigInteger().with_variant(Integer, "sqlite"), primary_key=True),
    Column("sender_id",Integer),
)

follows=Table(
    "follows",metadata,
    Column("id", BigInteger().with_variant(Integer, "sqlite"), primary_key=True),
    Column("follower_id",Integer, index=True),
    Column("followee_id",Integer),
)

user=Table(
    "user",metadata,
    Column("id", BigInteger().with_variant(Integer, "sqlite"), primary_key=True),
    Column("screen_name",String(250)),  # whatever
)


def start_mappers():
    tweets_mapper = mapper_registry.map_imperatively(models.Tweet, tweets)
    follow_mapper = mapper_registry.map_imperatively(models.Follow, follows)
    user_mapper = mapper_registry.map_imperatively(models.User,user)
