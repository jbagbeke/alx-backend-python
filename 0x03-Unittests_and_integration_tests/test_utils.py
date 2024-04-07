#!/usr/bin/env python3
"""
Unit Testing for utils module
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map


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
        self.assertEqual(access_nested_map(nested_map, path), result)
    
    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError):f
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
