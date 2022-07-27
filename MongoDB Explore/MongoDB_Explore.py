from pymongo import MongoClient
#import pymongo
import pandas as pd

CONNECTION_STRING = 'mongodb://admin:admin@192.168.182.140:27017/?authSource=test'
myclient = MongoClient(CONNECTION_STRING)

db_explore=pd.DataFrame()
for db in myclient.list_database_names():    
    dict={}
    mydb = myclient[db]
    #print("Database ------- "+str(db))
    dict["DB"]=db
    for col in mydb.list_collection_names():
        dict["col"]=col
        mycol = mydb[col]
        #print(" -- Collection ------- "+str(col))
        db_explore = db_explore.append(dict, ignore_index=True)
print(db_explore.head())