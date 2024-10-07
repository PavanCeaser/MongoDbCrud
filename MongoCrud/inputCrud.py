from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["crud"]
collection = db["operation"]

# Insert
def insert_document():
    document = {"name": "John", "age": 30}
    result = collection.insert_one(document)
    print(f"Inserted document ID: {result.inserted_id}")

# Read
def read_documents():
    documents = collection.find()
    for document in documents:
        print(document)

# Update
def update_document():
    filter = {"name": "John"}
    update = {"$set": {"age": 31}}
    result = collection.update_one(filter, update)
    print(f"Updated documents: {result.modified_count}")

# Delete
def delete_document():
    filter = {"name": "John"}
    result = collection.delete_one(filter)
    print(f"Deleted documents: {result.deleted_count}")

# Call the functions
insert_document()
read_documents()
update_document()
read_documents()  # To see the updated document
delete_document()
read_documents()  # To see the deleted document
# ``'


# **Pretty Print**


# Use the `pprint` function from the `pprint` module to print documents in a formatted way.


# ```python
# from pymongo import MongoClient
# from pprint import pprint

# # ...

# Read
def read_documents():
    documents = collection.find()
    for document in documents:
        pprint(document)