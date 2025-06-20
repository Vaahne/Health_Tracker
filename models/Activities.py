from config import db

activities = db["Activities"]

if "Activities" not in db.list_collection_names():
    db["Activities"].insert_one({"_temp": True})  # temporary dummy doc
    db["Activities"].delete_many({"_temp": True})  # clean up dummy docs


db.command({
    "collMod": "Activities",
    "validator": {
        "$jsonSchema": {
            "bsonType": "object",
            "required": ["type","description","caloriesPerTenMinutes","active","createdAt"],
            "properties":{
                "type": {"bsonType": "string"},
                "description": {"bsonType": "string"},
                "caloriesPerTenMinutes": {"bsonType": "number","minimum":1},
                "active": {"bsonType":"bool"},
                "createdAt": {"bsonType":"date"}
            }
        }
    }    
})