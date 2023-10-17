#!/usr/bin/env python3
""" The script to make a query based on a specific topic """


def schools_by_topic(mongo_collection, topic):
    """" THe function that fetches data based on topic """
    result = mongo_collection.find({"topic": topic})
    if result:
        return result
    return []
