#!/usr/bin/env python3
""" Redis Module """
import redis
import uuid
from typing import Union


class cache:
    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
