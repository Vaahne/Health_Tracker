from flask import request, jsonify,Blueprint
from models.ActivityTracker import activityTracker
from bson import ObjectId
from datetime import datetime

activityTrackerRouter = Blueprint("activityTrackerRouter",__name__)

@activityTrackerRouter.route('/add',methods=['POST'])
def add_activityTracker():
    try:
        print('adding')
        data = request.json
        data['userId'] = ObjectId(data['userId'])
        data['type'] = ObjectId(data['type'])
        if 'date' not in data:
            data['date'] = datetime.utcnow()
        activityTracker.insert_one(data)
        return jsonify({'msg':'Successfully added to the activity Tracker!!!'}),201
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!'}]}),500

@activityTrackerRouter.route('/delete/<activityTracker_id>',methods=['DELETE'])
def delete_activityTracker(activityTracker_id):
    try:
        print('Delete ')
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!'}]}),500

@activityTrackerRouter.route('/update/<activityTracker_id>',methods=['PUT'])
def update_activityTracker(activityTracker_id):
    try:
        print('Update')
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!'}]}),500

@activityTrackerRouter.route('/get',methods=['GET'])
def get_activityTracker():
    try:
        print('get all')
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!'}]}),500