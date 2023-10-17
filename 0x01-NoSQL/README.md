# MongoDB and Python

This repository contains a series of tasks related to MongoDB and Python.

## Task Descriptions

### Task 0: List all databases

**Mandatory**

Write a script that lists all databases in MongoDB.

```sh
guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/0x01$
```
File: [0-list_databases](./0-list_databases)

### 1: Create a database

**Mandatory**

Write a script that creates or uses the database `my_db`.

```sh
guillaume@ubuntu:~/0x01$ cat 0-list_databases | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
admin        0.000GB
config       0.000GB
local        0.000GB
logs         0.005GB
bye
guillaume@ubuntu:~/0x01$
guillaume@ubuntu:~/0x01$ cat 1-use_or_create_database | mongo
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
switched to db my_db
bye
guillaume@ubuntu:~/0x01$
```

File: [1-use_or_create_database](./1-use_or_create_database)

### 2: Insert document

**Mandatory**

Write a script that inserts a document in the collection `school`.

The document must have one attribute `name` with the value “Holberton school”.
The database name will be passed as an option of mongo command.

```sh
guillaume@ubuntu:~/0x01$ cat 2-insert | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nInserted" : 1 })
bye
guillaume@ubuntu:~/0x01$
```

File: [2-insert](./2-insert)

### 3: All documents

**Mandatory**

Write a script that lists all documents in the collection `school`.

The database name will be passed as an option of mongo command.

```sh
guillaume@ubuntu:~/0x01$ cat 3-all | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/0x01$
```

File: [3-all](./3-all)

### 4: All matches

**Mandatory**

Write a script that lists all documents with `name="Holberton school"` in the collection `school`.

The database name will be passed as an option of mongo command.

```sh
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school" }
bye
guillaume@ubuntu:~/0x01$
```

File: [4-match](./4-match)

### 5: Count

**Mandatory**

Write a script that displays the number of documents in the collection `school`.

The database name will be passed as an option of mongo command.

```sh
guillaume@ubuntu:~/0x01$ cat 5-count | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
1
bye
guillaume@ubuntu:~/0x01$
```

File: [5-count](./5-count)

### 6: Update

**Mandatory**

Write a script that adds a new attribute to a document in the collection `school`.

The script should update only documents with name="Holberton `school" (all of them)`.
The update should add the attribute `address` with the value “972 Mission street”.
The database name will be passed as an option of mongo command.

```sh
guillaume@ubuntu:~/0x01$ cat 6-update | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
WriteResult({ "nMatched" : 1, "nUpserted" : 0, "nModified" : 1 })
bye
guillaume@ubuntu:~/0x01$
guillaume@ubuntu:~/0x01$ cat 4-match | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a8fad532b69437b63252406"), "name" : "Holberton school", "address" : "972 Mission street" }
bye
guillaume@ubuntu:~/0x01$
```

File: [6-update](./6-update)

### 7: Delete by match

**Mandatory**

Write a script that deletes all documents with `name="Holberton school"` in the collection `school`.

The database name will be passed as an option of mongo command.

```sh
guillaume@ubuntu:~/0x01$ cat 7-delete | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "acknowledged" : true, "deletedCount" : 1 }
bye
guillaume@ubuntu:~/0x01$
```

File: [7-delete](./7-delete)

### 8: List all documents in Python

**Mandatory**

Write a Python function that lists all documents in a collection.

The collection name will be passed as an argument of the function.

Prototype: `def list_all(mongo_collection: Collection) -> List[Dict]`.

```python
guillaume@ubuntu:~/0x01$ cat 8-all.py
#!/usr/bin/env python3
""" 8. List all documents in Python """
from pymongo.collection import Collection
from typing import List, Dict


def list_all(mongo_collection: Collection) -> List[Dict]:
    """
    List all documents in a collection
    """
    return list(mongo_collection.find({}))

guillaume@ubuntu:~/0x01$
```

File: [8-all.py](./8-all.py)

### 9: Insert a document in Python

**Mandatory**

Write a Python function that inserts a new document in a collection based on `kwargs`.

Prototype: `def insert_school(mongo_collection: Collection, **kwargs) -> Dict`.

```python
guillaume@ubuntu:~/0x01$ cat 9-insert_school.py
#!/usr/bin/env python3
""" 9. Insert a document in Python """
from pymongo.collection import Collection
from typing import Dict


def insert_school(mongo_collection: Collection, **kwargs) -> Dict:
    """
    Insert a document in a collection based on kwargs
    """
    return {'_id': mongo_collection.insert_one(kwargs).inserted_id}

guillaume@ubuntu:~/0x01$
```

File: [9-insert_school.py](./9-insert_school.py)

### 10: Change school topics

**Mandatory**

Write a Python function that changes all topics of a school document based on the `name`.

Prototype: `def update_topics(mongo_collection: Collection, name: str, topics: List) -> None`.

```python
guillaume@ubuntu:~/0x01$ cat 10-update_topics.py
#!/usr/bin/env python3
""" 10. Change school topics """
from pymongo.collection import Collection
from typing import List


def update_topics(mongo_collection: Collection, name: str, topics: List) -> None:
    """
    Change school topics
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

guillaume@ubuntu:~/0x01$
```

File: [10-update_topics.py](./10-update_topics.py)

### 11: Where can I learn Python?

**Mandatory**

Write a Python function that returns the list of school having a specific topic.

Prototype: `def schools_by_topic(mongo_collection: Collection, topic: str) -> List`.

```python
guillaume@ubuntu:~/0x01$ cat 11-schools_by_topic.py
#!/usr/bin/env python3
""" 11. Where can I learn Python? """
from pymongo.collection import Collection
from typing import List


def schools_by_topic(mongo_collection: Collection, topic: str) -> List:
    """
    List of school having a specific topic
    """
    return list(mongo_collection.find({'topics': topic}))

guillaume@ubuntu:~/0x01$
```

File: [11-schools_by_topic.py](./11-schools_by_topic.py)

### 12: Log stats

**Mandatory**

Write a Python script that provides some stats about Nginx logs stored in MongoDB:

* Database: logs
* Collection: nginx
* Display (same as the example):
    * first line: x logs where x is the number of documents in this collection
    * second line: Methods:
    * 5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
    * one line with the number of documents with: method=GET path=/status

```sh
guillaume@ubuntu:~/0x01$ ./12-log_stats.py
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
```

File: [12-log_stats.py](./12-log_stats.py)

### 13: Regex filter

***Advanced***

Write a script that lists all documents with name starting by Holberton in the collection school:

The database name will be passed as an option of the mongo command.

```sh
guillaume@ubuntu:~/0x01$ cat 100-find | mongo my_db
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017/my_db
MongoDB server version: 3.6.3
{ "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton school" }
{ "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton School" }
{ "_id" : ObjectId("5a90731fd4321e1e5a3f53e3"), "name" : "Holberton-school" }
bye
```
File: [100-find](./100-find)

### 14: Top students

***Advanced***

Write a Python function that returns all students sorted by average score:

* Prototype: `def top_students(mongo_collection)`
* mongo_collection will be the pymongo collection object
* The top must be ordered
* The average score must be part of each item returned with key = averageScore

```python
guillaume@ubuntu:~/0x01$ cat 101-main.py
#!/usr/bin/env python3
""" 101-main """
from pymongo import MongoClient
list_all = __import__('8-all').list_all
insert_school = __import__('9-insert_school').insert_school
top_students = __import__('101-students').top_students

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students

    j_students = [
        { 'name': "John", 'topics': [{ 'title': "Algo", 'score': 10.3 },{ 'title': "C", 'score': 6.2 }, { 'title': "Python", 'score': 12.1 }]},
        { 'name': "Bob", 'topics': [{ 'title': "Algo", 'score': 5.4 },{ 'title': "C", 'score': 4.9 }, { 'title': "Python", 'score': 7.9 }]},
        { 'name': "Sonia", 'topics': [{ 'title': "Algo", 'score': 14.8 },{ 'title': "C", 'score': 8.8 }, { 'title': "Python", 'score': 15.7 }]},
        { 'name': "Amy", 'topics': [{ 'title': "Algo", 'score': 9.1 },{ 'title': "C", 'score': 14.2 }, { 'title': "Python", 'score': 4.8 }]},
        { 'name': "Julia", 'topics': [{ 'title': "Algo", 'score': 10.5 },{ 'title': "C", 'score': 10.2 }, { 'title': "Python", 'score': 10.1 }]}
    ]
    for j_student in j_students:
        insert_school(students_collection, **j_student)

    students = list_all(students_collection)
    for student in students:
        print("[{}] {} - {}".format(student.get('_id'), student.get('name'), student.get('topics')))

    top_students = top_students(students_collection)
    for student in top_students:
        print("[{}] {} => {}".format(student.get('_id'), student.get('name'), student.get('averageScore')))
```

File: [101-students.py](./101-students.py)

### 15: Log stats - new version

***Advanced***

Improve 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs:

* The IPs top must be sorted (like the example below)

```sh
guillaume@ubuntu:~/0x01$ ./102-log_stats.py
94778 logs
Methods:
    method GET: 93842
    method POST: 229
    method PUT: 0
    method PATCH: 0
    method DELETE: 0
47415 status check
IPs:
    172.31.63.67: 15805
    172.31.2.14: 15805
    172.31.29.194: 15805
    69.162.124.230: 529
    64.124.26.109: 408
    64.62.224.29: 217
    34.207.121.61: 183
    47.88.100.4: 166
    45.249.84.250: 160
    216.244.66.228: 150
```

File: [102-log_stats.py](./102-log_stats.py)
