from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Tweet:
    sender_id: int
    id: int | None = None


@dataclass
class User:
    id: int | None = None
    screen_name: str | None = None


@dataclass
class Follow:
    id: int | None = None
    follower_id: int | None = None
    followee_id: int | None = None
