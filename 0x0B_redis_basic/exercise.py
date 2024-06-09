#!/usr/bin/env python3
import uuid
import redis
from typing import Union, Callable
from functools import wraps


def count_calls(fn: Callable) -> Callable:
    """
    Count how many times a method is called
    """

    @wraps(fn)
    def wrapper(self, *args, **kwargs):
        key = fn.__qualname__
        if self._redis.exists(key):
            self._redis.incr(key)
        else:
            self._redis.set(key, 1)
        return fn(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    Cache class
    """
    def __init__(self):
        """
        Initialize Cache with an instance of Redis
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis
		"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[bytes, str, int, float]:
        """
        Get data from Redis
        """
        data = self._redis.get(key)
        if data is None:
            return data
        if fn is None:
            return data
        return fn(data)

    def get_str(self, key: str) -> str:
        """
        Get data from Redis as string
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Get data from Redis as integer
        """
        return self.get(key, fn=int)
