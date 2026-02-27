
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://praveenn:Praveen%40123@praveen.wfegu.mongodb.net/?appName=Praveen"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Connect to MongoDB
db = client["company_db"]  # Create or get the database
collection = db["employees"]  # Create or get the collection

def add_employee(name, age, department, salary):
    employee = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }
    collection.insert_one(employee)
    print(f"Employee {name} added successfully!")

# Example Usage:
add_employee("Alice", 30, "HR", 60000)
add_employee("Bob", 28, "IT", 80000)
add_employee("Charlie", 35, "Finance", 75000)
