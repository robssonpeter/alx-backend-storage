#!/usr/bin/env python3
""" THe scrip to read nginx logs from mongo db """
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017")

    print(f"{client.logs.nginx.count()} logs")
    print("Methods:")
    print(f"\tmethod GET: {client.logs.nginx.count({'method': 'GET'})}")
    print(f"\tmethod POST: {client.logs.nginx.count({'method': 'POST'})}")
    print(f"\tmethod PUT: {client.logs.nginx.count({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {client.logs.nginx.count({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {client.logs.nginx.count({'method': 'DELETE'})}")
    print(f"{client.logs.nginx.count({'path': '/status'})} status check")

