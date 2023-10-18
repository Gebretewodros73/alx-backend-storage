#!/usr/bin/env python3
"""
Test file for Cache class
"""
import unittest


Cache = __import__('exercise').Cache

class TestCache(unittest.TestCase):
    def test_store(self):
        cache = Cache()
        data = b"hello"
        key = cache.store(data)
        self.assertTrue(key)

    def test_get(self):
        cache = Cache()
        data = b"hello"
        key = cache.store(data)
        result = cache.get(key)
        self.assertEqual(result, data)

if __name__ == '__main__':
    unittest.main()
