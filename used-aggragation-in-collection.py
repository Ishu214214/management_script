import pymongo

CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/"  
client = pymongo.MongoClient(CONNECTION_STRING)

mydatabase = client['ishu_example'] 
mycollection=mydatabase['ishu_example'] 
mycollection2=mydatabase['ishu_example_1'] 


pipeline = [
    {
        "$lookup": {
            "from": "ishu_example",
            "localField": "_id",
            "foreignField": "customer_id",
            "as": "customer_info"
        }
    },
    {
        "$unwind": "$customer_info"
    },
    {
        "$project": {
            "order_id": "$_id",
            "customer_id": "$customer_id",
            "order_date": "$order_date",
            "total_amount": "$total_amount",
            "customer_name": "$customer_info.name",
            "customer_email": "$customer_info.email"
        }
    },
    {
         "$limit": 3 
    },
    {
         "$sort": { "order_id": -1 }
    },
    {
        "$addFields": {"new_field added": "ishu"}   # add a field
    },

    #  {
    #      "$count": "medium"      # it will direct provied the count 3 and no other output
    # } ,

    # {
    #     "$match": {"size": "medium"}  # this will only match result only
    # },
]

result = mycollection2.aggregate(pipeline)

for doc in result:
    print(doc)















##############################################################################


# import pymongo

# CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/"  
# client = pymongo.MongoClient(CONNECTION_STRING)

# mydatabase = client['ishu_example'] 
# mycollection=mydatabase['ishu_example'] 
# mycollection2=mydatabase['ishu_example_1'] 


# pipeline = [
#     {
#         "$lookup": {
#             "from": "ishu_example",
#             "localField": "_id",
#             "foreignField": "customer_id",
#             "as": "customer_info"
#         }
#     },
#     {
#         "$unwind": "$customer_info"
#     },
#     {
#         "$project": {
#             "order_id": "$_id",
#             "customer_id": "$customer_id",
#             "order_date": "$order_date",
#             "total_amount": "$total_amount",
#             "customer_name": "$customer_info.name",
#             "customer_email": "$customer_info.email"
#         }
#     },
#     {
#          "$limit": 3 
#     }
# ]

# result = mycollection2.aggregate(pipeline)

# for doc in result:
#     print(doc)