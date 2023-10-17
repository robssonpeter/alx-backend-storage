#!/usr/bin/env python3
""" A python script to insert a ne item """
import json


def insert_school(mongo_collection, **kwargs):
    """ THe function that will insert a new entry to db """
    inserted = mongo_collection.insert_one(kwargs)
    return inserted.inserted_id
