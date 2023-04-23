from dataclasses import dataclass


@dataclass
class Tweet:
    id:int
    sender_id: int


@dataclass
class User:
    id:int
    screen_name: str
    follower_id: int


@dataclass
class Follow:
    id: int
    follower_id: int
    followee_id: int
