#!/usr/bin/env python3
"""
Redis Cache Implementation
"""
import redis
from typing import Callable, Union
from functools import wraps
import uuid


class Cache:
    """
    Cache class to interact with Redis
    """

    def __init__(self):
        """
        Initialize Redis client and flush the instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """
        Store data in Redis with a random key and return the key

        Args:
            data: The data to be stored (str, bytes, int, or float)

        Returns:
            str: The generated random key

        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(
            self, key: str, fn: Callable = None
            ) -> Union[str, bytes, int, None]:
        """
        Retrieve data from Redis using the key

        Args:
            key (str): The key associated with the data
            fn (Callable, optional): A callable function
            to convert the data. Defaults to None.

        Returns:
            Union[str, bytes, int, None]: The retrieved data

        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieve data from Redis as string

        Args:
            key (str): The key associated with the data

        Returns:
            str: The retrieved data as a string

        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieve data from Redis as integer

        Args:
            key (str): The key associated with the data

        Returns:
            int: The retrieved data as an integer

        """
        return self.get(key, fn=int)

    @staticmethod
    def count_calls(method: Callable) -> Callable:
        """
        Decorator to count method calls

        Args:
            method (Callable): The method to be decorated

        Returns:
            Callable: The decorated method

        """
        key = method.__qualname__

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            self._redis.incr(key)
            return method(self, *args, **kwargs)

        return wrapper

    @staticmethod
    def call_history(method: Callable) -> Callable:
        """
        Decorator to store history of inputs and outputs

        Args:
            method (Callable): The method to be decorated

        Returns:
            Callable: The decorated method

        """
        key_inputs = f"{method.__qualname__}:inputs"
        key_outputs = f"{method.__qualname__}:outputs"

        @wraps(method)
        def wrapper(self, *args, **kwargs):
            self._redis.rpush(key_inputs, str(args))
            result = method(self, *args, **kwargs)
            self._redis.rpush(key_outputs, str(result))
            return result

        return wrapper
