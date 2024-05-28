#!/usr/bin/env python3
"""
This module contains unit tests for the GithubOrgClient class.
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
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
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org"""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with
        (GithubOrgClient.ORG_URL.format(org=org_name))

    @patch("client.get_json", return_value=[
        {"name": "Amazon"}, {"name": "Google"}
        ])
    def test_public_repos(self, mocked):
        """Test public_repo method"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock):
            self.assertEqual(GithubOrgClient('test').public_repos(),
                             ["Amazon", "Google"])
            mocked.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_return):
        """Test has_license method"""
        client = GithubOrgClient('test')
        self.assertEqual(client.has_license(repo, license_key), expected_return)


if __name__ == "__main__":
    unittest.main()
