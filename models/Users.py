from config import db

users = db["Users"]


db.command({
    "collMod": "Users",
    "validator": {
        "$jsonSchema":{
            "bsonType" : "object",
            "required" : ["name","email","password"],
            "properties": {
                "name": {"bsonType": "string"},
                "email": {"bsonType": "string", "pattern": "^.+@.+$"},
                "password": {"bsonType": "string", "minLength": 6},
                "createdAt": {"bsonType": "date"}
            }
        }
    }
})