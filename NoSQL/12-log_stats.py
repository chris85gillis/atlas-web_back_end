#!/usr/bin/env python3
"""
This script logs statistics about the logs collection in the logs database.
It prints the total number of logs, the number of logs for each HTTP method,
and the number of logs with method=GET and path=/status.
"""
from pymongo import MongoClient


def log_stats():
    # Connect to MongoDB
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Total number of logs
    total_logs = collection.count_documents({})

    # Methods count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    methods_count = {method: collection.count_documents({"method": method}) for method in methods}

    # Number of documents with method=GET and path=/status
    status_check = collection.count_documents({"method": "GET", "path": "/status"})

    # Output results
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {methods_count[method]}")
    print(f"{status_check} status check")

if __name__ == "__main__":
    log_stats()
