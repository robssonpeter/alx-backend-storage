#!/usr/bin/env python3
""" The script to get all elements from db """
from pymongo import MongoClient


def list_all(mongo_collection):
    """ The function that fetches all data from collection """

    data = mongo_collection.find()
    if data:
        return data
    return []
