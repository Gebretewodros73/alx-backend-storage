# Redis and Python Tasks

## Task 0: Writing strings to Redis

### Instructions
Create a Cache class that stores data in Redis. The class should have an __init__ method that initializes a Redis client and flushes the instance. Implement a store method that takes various data types and stores them in Redis with a random key.

Example usage:
```python
import redis

Cache = __import__('exercise').Cache

cache = Cache()

data = b"hello"
key = cache.store(data)
print(key)

local_redis = redis.Redis()
print(local_redis.get(key))
```

File: [exercise.py](/exercise.py)
## Task 1: Reading from Redis and recovering original type

### Instructions

Create a get method that retrieves data from Redis and optionally converts it back to the original format using a provided Callable function.

Example usage:

```python
cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
```

File: [exercise.py](/exercise.py)

## Task 2: Incrementing values

### Instructions

Implement a system to count how many times methods of the Cache class are called. Create a count_calls decorator that increments the count for each method call and returns the value returned by the original method.

Example usage:

```python
Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
```

File: [exercise.py](/exercise.py)

## Task 3: Storing lists

### Instructions

Implement a `call_history` decorator to store the history of inputs and outputs for a particular function. The decorator will append input parameters and output to separate lists in Redis.

Example usage:

```python
Cache = __import__('exercise').Cache

cache = Cache()

s1 = cache.store("first")
print(s1)
s2 = cache.store("second")
print(s2)
s3 = cache.store("third")
print(s3)

inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

print("inputs: {}".format(inputs))
print("outputs: {}".format(outputs))
```

File: [exercise.py](/exercise.py)

## Task 4: Retrieving lists

### Instructions

Implement a replay function to display the history of calls of a particular function using keys generated in previous tasks.

Example usage:

```python
cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
```

File: [exercise.py](/exercise.py)

## Task 5: Implementing an expiring web cache and tracker

### Instructions

Implement a get_page function that obtains the HTML content of a URL using the requests module. Track how many times a particular URL was accessed and cache the result with an expiration time of 10 seconds.

Example usage:

```python
from web import get_page

content = get_page("http://example.com")
print(content)
```

File: [web.py](/web.py)

