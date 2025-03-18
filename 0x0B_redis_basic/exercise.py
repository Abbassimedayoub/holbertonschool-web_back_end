#!/usr/bin/env python3
""" Redis Module """
import redis, Callable
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

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        # Récupère les données depuis Redis
        data = self._redis.get(key)

        # Si les données n'existent pas, on retourne None
        if data is None:
            return None

        # Si une fonction de conversion (fn) est fournie, on l'applique
        if fn:
            return fn(data)

        # Sinon, on retourne les données telles qu'elles sont (par défaut en tant que bytes)
        return data
