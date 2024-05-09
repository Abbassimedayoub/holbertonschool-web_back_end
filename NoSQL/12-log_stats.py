#!/usr/bin/env python3
'''
Python script to generate statistics about Nginx logs stored in MongoDB.
'''
from pymongo import MongoClient

def count(mongo_collection):
    '''Count documents in the collection.'''
    return mongo_collection.count_documents({})

def count_by_method(mongo_collection, method):
    '''Count documents by HTTP method.'''
    return mongo_collection.count_documents({"method": method})

if __name__ == "__main__":
    # Establish a connection to MongoDB using MongoClient.
    client = MongoClient('mongodb://127.0.0.1:27017')

    # Access the 'logs' database and 'nginx' collection.
    nginx = client.logs.nginx

    # Count total logs.
    total_logs = count(nginx)
    print("{} logs".format(total_logs))

    # Count logs for each HTTP method.
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        method_count = count_by_method(nginx, method)
        print("\t method {}: {}".format(method, method_count))

    # Count logs specifically for status check (GET method with path "/status").
    status_check_count = count_by_method(nginx, "GET")  # Assuming /status is a status check endpoint.
    print("{} status check".format(status_check_count))
