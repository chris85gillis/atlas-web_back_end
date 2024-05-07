#!/usr/bin/python3
""" MRU caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """ Defines a caching system using MRU (Most Recently Used) policy
    """

    def __init__(self):
        """ Initializes the MRU cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the most recently used item
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

        # Move the key to the end of the order list to indicate recent usage
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
