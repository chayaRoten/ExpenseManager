from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client['Budget_management']
users = db['users']
budget_management = db['budget_management']

