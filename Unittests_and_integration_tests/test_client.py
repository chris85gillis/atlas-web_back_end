#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json, access_nested_map, memoize

class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for the GithubOrgClient class.
    """
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        '''Test org'''
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with
        (GithubOrgClient.ORG_URL.format(org=org_name))


if __name__ == "__main__":
    unittest.main()
