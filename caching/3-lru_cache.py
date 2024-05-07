#!/usr/bin/python3
""" LRU caching module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ Defines a caching system using LRU (Least Recently Used) policy
    """

    def __init__(self):
        """ Initializes the LRU cache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the order when key exists
            self.order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            # Discard the least recently used item
            discarded_key = self.order.pop(0)
            del self.cache_data[discarded_key]
            print("DISCARD:", discarded_key)

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the order to reflect the recent usage
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
