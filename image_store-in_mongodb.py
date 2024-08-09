import pymongo
from pymongo import MongoClient
from bson import Binary
from PIL import Image
from io import BytesIO

# Connect to MongoDB
CONNECTION_STRING = "mongodb+srv://Ishu:P6TUnliSjFLH290x@copyproductdetail.bojn1so.mongodb.net/"  
client = pymongo.MongoClient(CONNECTION_STRING)

mydatabase = client['demo_copy_example_1'] 
collection = mydatabase['images']  # Specify the collection

with open('/home/chinmay/Pictures/2024-04-11_09-53.png', 'rb') as f:
    image_data = f.read()

binary_image = Binary(image_data)
"""     image insert    """
# collection.insert_one({'image': binary_image})

# print("Image uploaded with ID:")

"""     image read  """
image_document = collection.find_one()
binary_image = image_document['image']

image_bytes = BytesIO(binary_image)

image = Image.open(image_bytes)
print(1)
image.show()
print(image)