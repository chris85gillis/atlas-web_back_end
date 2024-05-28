#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests for the GithubOrgClient class.
    """
    @parameterized.expand([
        ('google',),
        ('abc',),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org, mock_get_json):
        """
        Test that the org attribute is correctly set.
        """
        client = GithubOrgClient(org)
        client.org
        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format(org=org))


if __name__ == "__main__":
    unittest.main()
