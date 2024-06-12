#!/usr/bin/env python3
""" Insert new document """


def insert_school(mongo_collection, **kwargs):
    """ Insert new document in collection based on kwargs. """
    new_school = mongo_collection.insert_one(kwargs).inserted_id
    return new_school
