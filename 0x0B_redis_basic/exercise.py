#!/usr/bin/env python3
import uuid
import redis
from typing import Union


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
