#!/usr/bin/env python3
""" Update document """
import pymongo
from typing import List


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name

        Args:
            mongo_collection: collection to pass
            name: school name to update
            topics: list of topics
    
        Return:
            Nothing
    """
    query: dict = {'name': name}
    mongo_collection.update_many(query, {'$set': {'topics': topics}})
