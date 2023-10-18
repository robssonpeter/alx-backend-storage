#!/usr/bin/env python3
""" The script to Create a Cache Class """
import redis
import uuid
from typing import Union


class Cache:
    """ The class cache for implementing redis """

    def __init__(self) -> None:
        self.__redis = redis.Redis()
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ The store method to generate a key """
        key = str(uuid.uuid4())

        if isinstance(data, (str, bytes)):
            self.__redis.set(key, data)
        elif isinstance(data, (int, float)):
            self.__redis.set(key, str(data))
        else:
            raise ValueError("type only str, bytes, int and float allowed")
        return key
