from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Tweet:
    sender_id: int
    id: int | None = None


@dataclass
class User:
    screen_name: str
    follower_id: int
    id: int | None = None


@dataclass
class Follow:
    follower_id: int
    followee_id: int
    id: int | None = None
