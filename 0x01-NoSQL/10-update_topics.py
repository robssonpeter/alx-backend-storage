#!/usr/bin/env python3
""" The script to update topics """


def update_topics(mongo_collection, name, topics):
    """ The updating topics function to be run """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
