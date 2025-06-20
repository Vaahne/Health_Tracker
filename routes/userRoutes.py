from flask import request , jsonify , Blueprint
from models.Users import users
from bson import ObjectId

userRouter = Blueprint("userRouter",__name__)

# adding a new user 
@userRouter.route('/add',methods=['POST'])
def add_user():
    try:
        print('Hello from adding user')
        data = request.json
        users.insert_one(data)
        return jsonify({'message': 'User added!'}),201
    except Exception as e:
        return jsonify({'errors' :[{msg:'Server error'}]}),500

# getting all users
@userRouter.route('/getusers',methods=['GET'])
def get_users():
    try:
        print('Hello from getting users')
        usersList = list(users.find({},{"_id":0,"password":0})) # Excluding mongodb _ids 
        return jsonify(usersList),200
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error'}]}),500

# deleting the user by user_id
@userRouter.route('/delete/<user_id>',methods=['DELETE'])
def delete_users(user_id):
    try:
        print('deleting a user',user_id)
        result = users.delete_one({"_id": ObjectId(user_id)})
        if result.deleted_count == 0 :
            return jsonify({'errors':[{'msg':'User not found'}]}),404
        return jsonify({'msg':'Successfully deleted the user!!'}),200
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!!'}]}),500