#!/usr/bin/env python3
"""
This script logs statistics about the logs collection in the logs database.
It prints the total number of logs, the number of logs for each HTTP method,
and the number of logs with method=GET and path=/status.
"""
from pymongo import MongoClient


def log_stats():
    """Connect to MongoDB and print statistics"""
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    collection = db["nginx"]

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    status_check_count = collection.count_documents({"method":
                                                    "GET", "path": "/status"})
    print(f"{status_check_count} status check")


if __name__ == "__main__":
    log_stats()
