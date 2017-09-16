# -*-coding:utf-8 -*-
import sys
import datetime
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)
db = client['test_database']
#  or use db = client.test_database
post = {
    "author": "Mike",
    "text": "My first blog test",
    "tags": ["MongoDB", "python", "pymongo"],
    "date": datetime.datetime.utcnow()
}

new_posts = [
    {
        "author": "Mike",
        "text": "Author post!",
        "tags": ["bulk", "insert"],
        "dates": datetime.datetime(2009, 11, 12, 11, 14)
    },
    {
        "author": "Eliot",
        "title": "MongoDB is fun",
        "text": "and pretty esay tool",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    }
]


def get(post_id_is):
    document = client.db.collection.find_one({
        "id": post_id
    })

posts = db.posts
post_id = posts.insert_one(post).inserted_id  # 获取post_id
post_id_as_str = str(post_id)
post_result = posts.insert_many(new_posts)

print(post_id)
print(posts.find_one())
print(posts.find_one({
    "author": "Mike",
    "id": post_id_as_str
}))
print(post_result.inserted_ids)
print(posts.count())
