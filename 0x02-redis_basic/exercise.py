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

    def get(self, key: str, fn: callable) -> str:
        """ The function to retrive a key from db """
        res = self.__redis.get(key)
        if res:
            return fn(res)
        return res

    def get_str(self, key: str) -> str:
        """ Parameterise the string """
        return self.get(key, str)

    def get_int(self, key: str) -> str:
        """ Parameterise the int from db """
        return self.get(key, int)
