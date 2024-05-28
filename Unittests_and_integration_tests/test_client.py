#!/usr/bin/env python3
"""
This module contains unit tests for the GithubOrgClient class.
"""
import unittest
import requests
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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


@parameterized_class((
    "org_payload", "repos_payload", "expected_repos",
    "appache2_reops"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up for the class"""
        parameters = {"return_value.json.side_effect": [
            cls.org_payload, cls.repos_payload,
        ]}
        cls.get_patcher = patch("requests.get", **parameters)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Stop the patcher after the test class has finished.
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """
        Test public_repo method for integration tests
        """
        client = GithubOrgClient("Google")
        self.assertEqual(client.public_repos(), self.expected_repos)


if __name__ == "__main__":
    unittest.main()
