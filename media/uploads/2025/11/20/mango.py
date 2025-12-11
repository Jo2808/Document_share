from pymongo import MongoClient

client = MongoClient('mongodb+srv://user_123:Suga_1234@cluster0.ljbqual.mongodb.net/?appName=Cluster0')
db = client['mydatabase']
collection = db['mango_collection']

collection.insert_one({'fruit': 'mango', 'color': 'yellow', 'taste': 'sweet'})

collection.insert_many([
    {'fruit': 'mango', 'color': 'green', 'taste': 'tart'},
    {'fruit': 'mango', 'color': 'red', 'taste': 'sweet'},
    {'fruit': 'mango', 'color': 'orange', 'taste': 'sweet-tart'},
    {'fruit': 'mango', 'color': 'purple', 'taste': 'exotic'},
    {'fruit': 'mango', 'color': 'pink', 'taste': 'fruity'},
])

for doc in collection.find():
    print(doc)

#findone
print("findone:", collection.find_one({'color': 'red'}))
#updateone
print("updateone:", collection.update_one({'color': 'green'}, {'$set': {'taste': 'very tart'}}).modified_count)
#updatemany
print("updatemany:", collection.update_many({'taste': 'sweet'}, {'$set': {'taste': 'delicious'}}).modified_count)
#deleteone
print("deleteone:", collection.delete_one({'color': 'pink'}).deleted_count)
#bulkwrite
#print("bulkwrite:", collection.bulk_write([
#    collection.UpdateOne({'color': 'orange'}, {'$set': {'taste': 'zesty'}}),
#    collection.DeleteOne({'color': 'purple'})
#]))
#countdocuments
print("countdocuments:", collection.count_documents({'fruit': 'mango'}))
#sort
print("sort:", list(collection.find().sort('color', 1)))
#distinct
print("distinct:", collection.distinct('taste'))