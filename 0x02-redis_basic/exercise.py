#!/usr/bin/env python3
"""
Cache module for basic Redis operations
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class to interact with Redis
    """
    def __init__(self):
        """
        Initializes a Redis client and flushes the database
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores input data in Redis and returns the generated key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
