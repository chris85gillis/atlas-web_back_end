#!/usr/bin/env python3
import unittest
from unittest.mock import patch
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
        """Test org"""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with
        (GithubOrgClient.ORG_URL.format(org=org_name))

    @patch.object(GithubOrgClient, 'org',
                  return_value={'repo_url': 'https://github.com/test/repo'})
    def test_public_repos_url(self, mock_org):
        """Test that the public_repos_url property returns
        the expected repo_url from the org method.
        """
        client = GithubOrgClient('test')
        result = client._public_repos_url
        self.assertEqual(result, 'https://github.com/test/repo')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test GithubOrgClient.public_repos method.
        """
        payload = [
            {'name': 'repo1'},
            {'name': 'repo2'},
            {'name': 'repo3'}
        ]
        mock_get_json.return_value = payload
        client = GithubOrgClient('testorg')
        result = client.public_repos()
        mock_get_json.assert_called_once_with
        ("https://api.github.com/orgs/testorg/repos")


if __name__ == "__main__":
    unittest.main()
