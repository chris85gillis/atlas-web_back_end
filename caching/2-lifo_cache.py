#!/usr/bin/python3
""" LIFO caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ Defines a caching system using LIFO (Last In, First Out) policy
    """

    def __init__(self):
        """ Initializes the LIFO cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            if self.order:
                discarded_key = self.order.pop()
                del self.cache_data[discarded_key]
                print("DISCARD:", discarded_key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
