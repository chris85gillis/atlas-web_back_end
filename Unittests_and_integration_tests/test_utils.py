#!/usr/bin/env python3
"""
Unit tests for utils module.
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import get_json, access_nested_map, memoize


class TestGetJson(unittest.TestCase):
    """
    Unit tests for the function get_json in utils.py
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Tests the function get_json from utils.py.

        Args:
            test_url (str): The URL to test.
            test_payload (dict): The expected JSON payload.
        """
        with patch('utils.requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)

            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


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
        Args:
            nested_map (dict): The nested map to test.
            path (tuple): The path of keys to access.
            expected: The expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


    @parameterized.expand([
        ({}, ('a',)),
        ({'a': 1}, ('a', 'b'))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests that access_nested_map raises a KeyError for the given inputs.
        Args:
            nested_map (dict): The nested map to test.
            path (tuple): The path of keys to access.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the memoize decorator in utils.py
    """
    def test_memoize(self):
        """
        Tests the memoize decorator from utils.py.
        """
        class TestClass:
            """
            A test class for memoize decorator.
            """
            def a_method(self):
                """
                A method that returns 42.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A memoized property that returns the result of a_method.
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()

            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
