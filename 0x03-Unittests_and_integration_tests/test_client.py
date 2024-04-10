#!/usr/bin/env python3
"""
GITHUB CLIENT TESTING
"""
import unittest
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
        """
        Testing org function of client module
        """
        json_mock.return_value.json.return_value = "https://holberton.io"

        test_client = GithubOrgClient(org_name)
        test_client.org
        test_client.org

        json_mock.assert_called_once()

    def test_public_repos_url(self):
        """
        Test for _public_repos_url property function
        """
        test_client = GithubOrgClient("google")

        with patch.object(GithubOrgClient,
                          'org',
                          new={"repos_url": "https://api.github.com/repos"}):

            self.assertEqual(test_client._public_repos_url,
                             "https://api.github.com/repos")

    def test_public_repos(self):
        """
        Testing public_repos function of client module
        """
        with patch('client.get_json') as get_function:
            get_function.return_value = \
                {"repos_url": "https://api.github.com/repos"}

            test_client = GithubOrgClient("google")

            with patch.object(GithubOrgClient,
                              '_public_repos_url',
                              new="https://api.github.com/repos"):
                self.assertEqual(test_client._public_repos_url,
                                 test_client.org["repos_url"])
                self.assertEqual(test_client._public_repos_url,
                                 test_client.org["repos_url"])
                self.assertEqual(test_client._public_repos_url,
                                 test_client.org["repos_url"])

            get_function.assert_called_once()
