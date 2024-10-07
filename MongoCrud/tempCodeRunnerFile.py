#read

# # Find a single document
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

    