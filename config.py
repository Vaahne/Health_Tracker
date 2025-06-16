import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# From environment variables
mongoURI = os.getenv('mongoURI')
# Connect to local MongoDB
client = MongoClient(mongoURI)

# Define DB and collection
db = client['HealthTracker']
collection = db["Users"]