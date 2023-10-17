#!/usr/bin/env python3
""" The script to make a query based on a specific topic """


def schools_by_topic(mongo_collection, topic):
    """" THe function that fetches data based on topic """
    return list(mongo_collection.find({"topic": topic}))