from pymongo import MongoClient
#import pymongo
import pandas as pd
import json
import ast
import json

CONNECTION_STRING = 'mongodb://admin:admin@192.168.182.140:27017/?authSource=test'
#mongodb://[username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
#https://docs.mongodb.com/manual/reference/connection-string/
myclient = MongoClient(CONNECTION_STRING)

#print(myclient.list_database_names())
mydb = myclient["Indeed"]
#print(mydb.list_collection_names())
mycol = mydb["Jobs_1"]


#myquery = { "name": { "$regex": "test" }, "address": "test4" }
mydoc = mycol.find({},{ "_id": 0 })
#mydoc = mycol.find_one({},{ "_id": 0, "name": 1, "address": 1 })
#print(list(mydoc.keys()))
#print(json.dumps(list(mydoc)))
output = pd.DataFrame(list(mydoc))
#print(list(mydoc))
#x=json.dumps(list(mydoc))
print(output)
#print("======================")
#works_data = pd.json_normalize(list(mydoc))
#print(works_data)