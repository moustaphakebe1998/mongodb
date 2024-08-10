#!/usr/bin/env python3

import os
import json
import pymongo
from datetime import datetime,timedelta

client=pymongo.MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.1.1")

db=client["test"]
collection=db["projet"]

chemin="/home/kebe"
for filename in os.listdir(chemin):
    if filename.endswith(".json"):
        filepath = os.path.join(chemin, filename)
        with open(filepath, 'r') as file:
            data = json.load(file)
        collection.insert_one(data)
        os.remove(filepath)
client.close()
