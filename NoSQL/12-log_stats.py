#!/usr/bin/env python3
"""
This script connects to a MongoDB instance running locally and counts the
number of documents in the "nginx" collection. It also counts the number of
documents for each HTTP method and the number of status checks.
"""
import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["logs"]
collection = db["nginx"]

count = collection.count_documents({})

get_count = collection.count_documents({"method": "GET"})
post_count = collection.count_documents({"method": "POST"})
put_count = collection.count_documents({"method": "PUT"})
patch_count = collection.count_documents({"method": "PATCH"})
delete_count = collection.count_documents({"method": "DELETE"})

status_count = collection.count_documents({"method": "GET", "path": "/status"})

print(str(count) + " logs")
print("Methods:")
print("\tmethod GET: " + str(get_count))
print("\tmethod POST: " + str(post_count))
print("\tmethod PUT: " + str(put_count))
print("\tmethod PATCH: " + str(patch_count))
print("\tmethod DELETE: " + str(delete_count))
print(str(status_count) + " status check")
