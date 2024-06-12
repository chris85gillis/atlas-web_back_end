#!/usr/bin/env python3
"""
Log stats
"""
import pymongo


def log_stats():
    """
    This function connects to a MongoDB instance running locally and counts
    the number of documents in the "nginx" collection. It also counts the
    number of documents for each HTTP method and the number of status checks.
	"""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["logs"]
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
