from flask import Blueprint, request , jsonify
from models.Goals import goals
from bson import ObjectId
from datetime import datetime

goalRouter = Blueprint("goalRouter",__name__)

# Getting all the goals
@goalRouter.route('/getgoals',methods=['GET'])
def get_goals():
    try:
        print('getting goals')
        data = goals.find({})
        return jsonify(data)
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!!'}]}),500

# add goal
@goalRouter.route('/add',methods=['POST'])
def add_goal():
    try:
        print('Hello from adding goal')
        data = request.json
        data['userId'] = ObjectId(data['userId'])
        data['type'] = ObjectId(data['type'])
        data['startDate'] = datetime.strptime(data['startDate'], '%d-%m-%Y')
        data['endDate'] = datetime.strptime(data['endDate'], '%d-%m-%Y')
        if 'createdAt' not in data:
            data['createdAt'] = datetime.utcnow()
        if 'completed' not in data:
            data['completed'] = False
        goals.insert_one(data)
        return jsonify({'message': 'Goal added!'}),201
    except Exception as e:
        return jsonify({'errors' :[{'msg':'Server error'}]}),500
    
# Delete a goal
@goalRouter.route('/delete/<goal_id>',methods=['DELETE'])
def delete_goal(goal_id):
    try:
        print('Deleting a goal by goal_id')
        res = goals.delete_one({"_id":ObjectId(goal_id)})
        if res.deleted_count == 0:
            return jsonify({'errors':[{'msg':'Goal doesnt exist!!'}]}),404
        return jsonify({'message': 'Goal Deleted !'}),201
    except Exception as e:
        return jsonify({'errors' :[{'msg':'Server error'}]}),500

# Update a goal
@goalRouter.route('/update/<goal_id>',methods=['PUT'])
def update_goal(goal_id):
    try:
        print('Updating a goal by goal_id')
        data = request.json
        updated_goal = {
            "startDate" : data.get('startDate'),
            "endDate": data.get("endDate"),
            "type": ObjectId(data.get("type")),
            "completed": data.get("completed",False)
        }
        res = goals.update_one({"_id":ObjectId(goal_id)},{"$set":updated_goal})
        if res.matched_count == 0:
            return jsonify({'errors':[{'msg':'Goal doesnt exist!!'}]}),404
        return jsonify({'message': 'Goal Updated!'}),200
    except Exception as e:
        return jsonify({'errors' :[{'msg':'Server error'}]}),500