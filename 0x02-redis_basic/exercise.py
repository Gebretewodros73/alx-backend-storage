#!/usr/bin/env python3
"""
Cache Class for Redis Operations
"""
import redis
import uuid
from typing import Callable, Union


class Cache:
    """
    Cache class to interact with Redis.
    """
    def __init__(self):
        """
        Initialize Cache instance with Redis client and flush the database.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, None]:
        """
        Retrieve data from Redis using the provided key.
        Optionally, apply a conversion function `fn` to the data.
        """
        data = self._redis.get(key)
        if data is not None and fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """
        Retrieve data from Redis and convert it to a string.
        """
        return self.get(key, fn=lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """
        Retrieve data from Redis and convert it to an integer.
        """
        return self.get(key, fn=int)
