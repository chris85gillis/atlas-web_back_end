#!/usr/bin/env python3
"""Update topics."""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a specific user in the database.
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
