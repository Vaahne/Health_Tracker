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

# delete from activty tracker
@activityTrackerRouter.route('/delete/<activityTracker_id>',methods=['DELETE'])
def delete_activityTracker(activityTracker_id):
    try:
        print('Delete from activity tracker')
        res = activityTracker.delete_one({'_id':ObjectId(activityTracker_id)})
        if res.deleted_count == 0:
            return jsonify({'errors':[{'msg':'Id not found'}]}),404
        return jsonify({'msg':'Successfully deleted from activity tracker'})
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!'}]}),500

# update by id to the activity tracker
@activityTrackerRouter.route('/update/<activityTracker_id>',methods=['PUT'])
def update_activityTracker(activityTracker_id):
    try:
        print('Update')
        data = request.json
        res = activityTracker.update_one({'_id':ObjectId(activityTracker_id)},{'$set':data})
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!'}]}),500

# get from activity tracker
@activityTrackerRouter.route('/get',methods=['GET'])
def get_activityTracker():
    try:
        print('get all')
        res = list(activityTracker.find({},{'_id':0}))
        return jsonify(res),200
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!'}]}),500