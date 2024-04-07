#!/usr/bin/python3
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
        print(nested_map)
        self.assertEqual(access_nested_map(nested_map, path), result)


if __name__ == '__main__':
    unittest.main()
