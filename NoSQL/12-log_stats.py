#!/usr/bin/env python3
"""
12-log_stats.py

Provides stats about Nginx logs stored in MongoDB:
Database: logs
Collection: nginx
"""

from pymongo import MongoClient


def main():
    """Print stats about nginx logs in MongoDB."""
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Total number of logs
    total = collection.count_documents({})
    print(f"{total} logs")

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    counts = {m: 0 for m in methods}

    # Count each method using aggregation
    pipeline = [
        {"$group": {"_id": "$method", "count": {"$sum": 1}}}
    ]
    for doc in collection.aggregate(pipeline):
        method = doc.get("_id")
        if method in counts:
            counts[method] = doc.get("count", 0)

    for m in methods:
        print(f"\tmethod {m}: {counts[m]}")

    # Count status checks
    status = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")


if __name__ == "__main__":
    main()
