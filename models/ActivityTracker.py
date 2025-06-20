from config import db

activityTracker = db["ActivityTracker"]

if "ActivityTracker" not in db.list_collection_names():
    db["ActivityTracker"].insert_one({"_temp": True})  # temporary dummy doc
    db["ActivityTracker"].delete_many({"_temp": True})  # clean up dummy docs


db.command({
    "collMod": "ActivityTracker",
    "validator":{
        "$jsonSchema":{
            "bsonType": "object",
            "required": ["userId","type","totalTimeofActivity","date"],
            "properties":{
                "userId": {"bsonType": "objectId" , "description": "References users._id"},
                "type": {"bsonType": "objectId" , "description": "References activities._id"},
                "totalTimeofActivity": {"bsonType": "number" , "minimum": 1},
                "date": {"bsonType": "date"}
            }
        }    
    }
})