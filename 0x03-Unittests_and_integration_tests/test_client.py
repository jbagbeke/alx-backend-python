#!/usr/bin/env python3
"""
GITHUB CLIENT TESTING
"""
import unittest
from utils import get_json, access_nested_map, memoize
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    Testing for github client
    """
    @parameterized.expand([("google"), ("abc")])
    @patch('requests.get')
    def test_org(self, org_name, json_mock):
        json_mock.return_value.json.return_value = "https://holberton.io"

        test_client = GithubOrgClient(org_name)
        test_client.org
        test_client.org

        json_mock.assert_called_once()

    def test_public_repos_url(self):
        test_client = GithubOrgClient("google")

        with patch.object(GithubOrgClient, 'org', new=
                {"repos_url": "https://api.github.com/repos"}):

            self.assertEqual(test_client._public_repos_url,
                             "https://api.github.com/repos")
