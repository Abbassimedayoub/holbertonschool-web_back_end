#!/usr/bin/env python3
""" Redis Module """
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in Redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
    def get(self, key: str,
        fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
    """ Get data from Redis """
    value = self._redis.get(key)
    return value if not fn else fn(value)
    