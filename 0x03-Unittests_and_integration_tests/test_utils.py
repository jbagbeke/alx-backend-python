#!/usr/bin/env python3
"""
Unit Testing for utils module
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Test Cases for utils module
    """

    @parameterized.expand([
        ({"a": 1}, "a", 1),
        ({"a": {"b": 2}}, "a", {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """
        Nested map test with parameterzation
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Nested map exception testing
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Testing Get JSON function in utils.py
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, payload, mock_get):
        """
        Get json function testing and mock of requests.get
        """
        mock_get.return_value.json.return_value = payload
        self.assertEqual(get_json(test_url), payload)


class TestMemoize(unittest.TestCase):
    """
    Testing memoize function of utils.py
    """

    def test_memoize(self):
        """
        Testing memoize function
        """

        class TestClass:
            """
            Test class to test memoize function
            """
            def a_method(self):
                """
                a_method function - a test function
                """
                return 42

            @memoize
            def a_property(self):
                """
                a_propoerty wrapped in memoize function
                """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as method_mock:
            method_mock.return_value = 42

            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)

            method_mock.assert_called_once()
