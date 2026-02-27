
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://praveenn:Praveen%40123@praveen.wfegu.mongodb.net/?appName=Praveen"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Connect to MongoDB
db = client["company_db"]  # Create or get the database
collection = db["employees"]  # Create or get the collection
for x in collection.find():
  print(x)