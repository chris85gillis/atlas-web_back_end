#!/usr/bin/env python3
"""
This script logs statistics about the logs collection in the logs database.
It prints the total number of logs, the number of logs for each HTTP method,
and the number of logs with method=GET and path=/status.
"""
from pymongo import MongoClient


def log_stats():
    """Connect to MongoDB and print statistics"""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_count = {method: collection.count_documents({"method": method}) for method in methods}

    status_check = collection.count_documents({"method": "GET", "path": "/status"})

    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {methods_count[method]}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
