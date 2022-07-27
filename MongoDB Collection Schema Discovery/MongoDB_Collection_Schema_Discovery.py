from pymongo import MongoClient
#import pymongo
import pandas as pd
import json
from genson import SchemaBuilder

CONNECTION_STRING = 'mongodb://admin:admin@192.168.182.140:27017/?authSource=test'
myclient = MongoClient(CONNECTION_STRING)

schema_discovery=pd.DataFrame()
for db in myclient.list_database_names():    
    dict={}
    mydb = myclient[db]
    print("Database ------- "+str(db))
    dict["DB"]=db
    if db == "admin" or db == "local":
        pass
    else:
        for col in mydb.list_collection_names():
            dict["col"]=col
            mycol = mydb[col]
            print(" -- Collection ------- "+str(col))
            #doc = mycol.find_one({},{ "_id": 0})
            #print(doc)
            docs = mycol.find({},{ "_id": 0}).limit(5)            
            docs_list=[]
            for doc in docs:
                docs_list.append(doc)
            builder = SchemaBuilder()
            builder.add_object(docs_list)
            schema_dict=builder.to_schema()
            schema_dict.pop("$schema")
            dict["schema"]=schema_dict
            print(json.dumps(schema_dict, sort_keys=True, indent=4))
            print("-------------------------------------------------------\n")

        schema_discovery = schema_discovery.append(dict, ignore_index=True)
print(schema_discovery.head().to_string())