from config import db

activityTracker = db["ActivityTracker"]

db.command({
    "collMod": "ActivityTracker",
    "$jsonSchema":{
        "bsonType": "object",
        "required": ["userId","type","totalTimeofActivity","date"],
        "properties":{
            "userId": {"bsonType": "objectId" , "Description": "References users._id"},
            "type": {"bsonType": "objectId" , "Desciption": "References activities._id"},
            "totalTimeofActivity": {"bsonType": "number" , "minimum": 1},
            "date": {"bsonType": "date"}
        }
    }    
})