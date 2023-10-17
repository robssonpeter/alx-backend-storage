#!/usr/bin/env python3
""" THe scrip to read nginx logs from mongo db """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")

    print(f"{client.logs.nginx.count_documents({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {client.logs.nginx.count_documents({'method': 'GET'})}")
    print(f"\tmethod POST: {client.logs.nginx.count_documents({'method': 'POST'})}")
    print(f"\tmethod PUT: {client.logs.nginx.count_documents({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {client.logs.nginx.count_documents({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {client.logs.nginx.count_documents({'method': 'DELETE'})}")
    print(f"{client.logs.nginx.count_documents({'path': '/status'})} status check")

