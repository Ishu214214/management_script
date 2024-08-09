
import pymongo
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
from pymongo import InsertOne

CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/"  
client = pymongo.MongoClient(CONNECTION_STRING)

mydatabase = client['1_copy_example_1'] 
mycollection=mydatabase['copy_example_1'] 


b2 ={ "ishu1":"ishuB0B" ,"A":3210}
b3 = { "ishu1":"B0B99CQ1" ,"A":1}
b4 = { "ishu1":"uQa1" ,"A":334322}

a= [b2 ,b3,b4]

operations = [InsertOne(doc) for doc in a]

"""      output
[InsertOne({'ishu1': 'ishuB0B', 'A': 3210}), InsertOne({'ishu1': 'B0B99CQ1', 'A': 1}), InsertOne({'ishu1': 'uQa1', 'A': 334322})]
"""
#print(operations)


try:
    result = mycollection.bulk_write(operations, ordered=False)
    print(result.inserted_count, "documents inserted.")
except BulkWriteError as e:
    # Handle duplicate key errors
    print("Duplicate key error occurred.")




filter = {  "ishu": "ubuy_B0B99BH3CQ1","A": 2}
replacement = {"name": "new_valu1e", "A": 1219833}
result = mycollection.replace_one(filter, replacement, upsert=True)
print("Upserted document ID:", result.upserted_id)
