#!/usr/bin/env python3
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Unit tests for the function access_nested_map in utils.py
    """
    @parameterized.expand([
        ({'a': 1}, ('a',), 1),
        ({'a': {'b': 2}}, ('a',), {'b': 2}),
        ({'a': {'b': 2}}, ('a', 'b'), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Tests the function access_nested_map from utils.py.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    
    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests that access_nested_map raises a KeyError for the following inputs.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


if __name__ == "__main__":
    unittest.main()
