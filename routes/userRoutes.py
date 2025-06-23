from flask import request , jsonify , Blueprint ,g
from models.Users import users
from bson import ObjectId
from utils.auth import generate_token , token_required
from datetime import datetime
import bcrypt

userRouter = Blueprint("userRouter",__name__)

# adding a new user 
@userRouter.route('/register',methods=['POST'])
def register_user():
    try:
        print('Hello from adding user')
        data = request.json
        
        existed_user = users.find_one({'email':data['email']})
        if existed_user:
            return jsonify({'errors':[{'msg':'User already exists!!'}]}),409

        # Hashing Password 
        password = data['password'].encode('utf-8')
        hashed_pw = bcrypt.hashpw(password,bcrypt.gensalt())
        # decoding to store as string in database
        data['password'] = hashed_pw.decode('utf-8')

        new_user = users.insert_one(data)
        user_id = str(new_user.inserted_id)

        token = generate_token(user_id)

        return jsonify({'message': 'User added!',
                        'token': token}),201
    except Exception as e:
        print('Error',e)
        return jsonify({'errors' :[{'msg':'Server error'}]}),500

# getting all users
@userRouter.route('/getusers',methods=['GET'])
def get_users():
    try:
        print('Hello from getting users')
        usersList = list(users.find({},{"_id":0,"password":0})) # Excluding mongodb _ids 
        return jsonify(usersList),200
    except Exception as e:
        print('Error',e)
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
        print('Error',e)
        return jsonify({'errors':[{'msg':'Server Error!!!'}]}),500

# Logging user
@userRouter.route('/login',methods=['POST'])
def user_login():
    try:
        data = request.json
        user_check = users.find_one({'email':data['email']})
    
        if not user_check:
            return jsonify({'errors':[{'msg':'Invalid credentials'}]}),404

        if not bcrypt.checkpw(data['password'].encode('utf-8'),user_check['password'].encode('utf-8')):
            return jsonify({'errors':[{'msg':'Invalid credentials'}]}),401
        
        token = generate_token(str(user_check['_id']))
        return jsonify({'msg':'Logged in success!!',
                        'token':token}),200
    except Exception as e:
        print('Exception ',e)
        return jsonify({'errors':[{'msg':'Server Error!'}]}),500

# Changing Password
@userRouter.route('changepwd',methods=['PUT'])
@token_required
def change_pwd():
    try :
        data = request.json
        user_id = ObjectId(g.user)  # from the decoded token (which gets from the header)
        res = users.find_one({'_id':user_id})
        if not res:
            return jsonify({'errors':[{'msg':'User not found'}]}),404
        
        if not bcrypt.checkpw(data['password'].encode('utf-8'),res['password'].encode('utf-8')):
            return jsonify({'errors':[{'msg':'Old password doesnot match'}]}),401
        
        # hashing the new password
        new_password = data['new_password'].encode('utf-8')
        hashed_pw = bcrypt.hashpw(new_password,bcrypt.gensalt())
        data['new_password'] = hashed_pw.decode('utf-8')

        result = users.update_one({'_id':user_id},{'$set':{'password':data['new_password']}})
        if result.matched_count == 0:
            return jsonify({'errors':[{'msg':'Update failed'}]}),400

        return jsonify({'msg':'Password changed succesfully!!'}),200
    except Exception as e:
        print('Exception: ',e)
        return jsonify({'errors':[{'msg':'Server Error!!'}]}),500
