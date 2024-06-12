#!/usr/bin/env python3
"""Update topics."""


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a specific user in the database.
    """
    query = {"name": name}
    new_values = {"$set": {"topics": topics}}
    mongo_collection.update_many(query, new_values)
