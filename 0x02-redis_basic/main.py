#!/usr/bin/env python3
"""
Main file
"""

# Import the Cache class
from exercise import Cache

# Create an instance of Cache
cache = Cache()

# Store data and get the generated key
key1 = cache.store(b"first")

# Retrieve data using the key and print it
data1 = cache.get(key1)
print(data1)

# Store more data
key2 = cache.store(b"second")
key3 = cache.store(b"third")

# Retrieve the stored data and print it
data2 = cache.get(key2)
data3 = cache.get(key3)

print(data2)
print(data3)
