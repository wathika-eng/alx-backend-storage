#!/usr/bin/env python3
"""Exercise: Python and Redis"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """
    Cache class
    """

    def __init__(self):
        """
        Initialize cache instance
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis
        Args:
            data: data to store
        Returns:
            str: key to access stored data
        """
        key = str(uuid4())
        self._redis.set(key, data)
        return key
