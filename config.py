import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# From environment variables
mongoURI = os.getenv('mongoURI')
SECRET_KEY = os.getenv('SECRET_KEY')
# Connect to local MongoDB
client = MongoClient(mongoURI)

# Define DB and collection
db = client['HealthTracker']

# Schemas of different collections
# schemas = {
#     "Activities":{
        
#     }
# }
# # collection = db["Users"]

# # Apply schema for each collection
# for collection , schema in schemas.items():
#     db.command({
#         "collMod": collection,
#         "validator": schema
#     })