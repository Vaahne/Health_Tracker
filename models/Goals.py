from config import db

goals = db["Goals"]

if "Goals" not in db.list_collection_names():
    db["Goals"].insert_one({"_temp": True})  # temporary dummy doc
    db["Goals"].delete_many({"_temp": True})  # clean up dummy docs

db.command({
    "collMod": "Goals",
    "validator": {
        "$jsonSchema":{
            "bsonType": "object",
            "required": ["userId","type","startDate","endDate","createdAt"],
            "properties":{
                "userId":{"bsonType":"objectId", "description": "References users._id"},
                "type": {"bsonType": "objectId", "description": "References activities._id"},
                "startDate": {"bsonType": "date"},
                "endDate": {"bsonType": "date"},
                "completed": {"bsonType":"bool"},
                "createdAt": {"bsonType": "date"}
            }
        },
    },
    "validationLevel" : "strict",
    "validationAction": "error"
})