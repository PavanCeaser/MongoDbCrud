from pymongo import MongoClient

# Replace the uri string with your MongoDB deployment's connection string.
client = MongoClient("mongodb://localhost:27017/")

# Get a reference to the database
db = client["crud"]

# Get a reference to the collection
collection = db["operation"]

#creat
# Insert a single document
# def create_document(collection, data):
#     result = collection.insert_one(data)
#     print(f"Inserted document ID: {result.inserted_id}")

# # Insert multiple documents
# def create_documents(collection, data_list):
#     result = collection.insert_many(data_list)
#     print(f"Inserted document IDs: {result.inserted_ids}")

# # Example usage
# data = {"name": "John", "age": 30}
# data_list = [{"name": "Jane", "age": 25}, {"name": "Bob", "age": 40}]

# create_document(collection, data)
# create_documents(collection, data_list)

# #read

# Find a single document
# def read_document(collection, filter):
#     document = collection.find_one(filter)
#     print(document)

# # Find multiple documents
# def read_documents(collection, filter):
#     documents = collection.find(filter)
#     for document in documents:
#         print(document)

# # Example usage
# filter = {"name": "John"}
# read_document(collection, filter)
# read_documents(collection, {})


# #update
# # Update a single document
# def update_document(collection, filter, update):
#     result = collection.update_one(filter, update)
#     print(f"Updated documents: {result.modified_count}")

# # Update multiple documents
# def update_documents(collection, filter, update):
#     result = collection.update_many(filter, update)
#     print(f"Updated documents: {result.modified_count}")

# # Example usage
# filter = {"name": "John"}
# update = {"$set": {"age": 31}}
# update_document(collection, filter, update)

# filter = {"age": {"$gt": 30}}
# update = {"$inc": {"age": 1}}
# update_documents(collection, filter, update)


# #delete
# # Delete a single document
# def delete_document(collection, filter):
#     result = collection.delete_one(filter)
#     print(f"Deleted documents: {result.deleted_count}")

# # Delete multiple documents
# def delete_documents(collection, filter):
#     result = collection.delete_many(filter)
#     print(f"Deleted documents: {result.deleted_count}")

# # Example usage
# filter = {"name": "John"}
# delete_document(collection, filter)

# filter = {"age": {"$lt": 30}}
# delete_documents(collection, filter)

# #file handling

# # try:
# #     # CRUD operation
# # except pymongo.errors.OperationFailure as e:
# #     print(f"Error: {e}")

    