from flask import Blueprint , request , jsonify
from models.Activities import activities
from bson import ObjectId
from datetime import datetime

activityRouter = Blueprint("activityRouter",__name__)

# adding new activity
@activityRouter.route('/add',methods=['POST'])
def add_activity():
    try:
        print('Adding activity')
        data =  request.json
        data['createdAt'] = datetime.utcnow()
        activities.insert_one(data)
        return jsonify({'msg':'Activity added successfully'})
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!!'}]}),500

# getting new activities
@activityRouter.route('/getactivities',methods=['GET'])
def get_activities():
    try:
        print('Getting the activities')
        res = list(activities.find({}))
        return jsonify(res)
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!!'}]}),500
    
# deleting the activity
@activityRouter.route('/delete/<activity_id>',methods=['DELETE'])
def delete_activity(activity_id):
    try:
        print(f'Deleting an activity!! {activity_id}')
        res = activities.delete_one({'_id': ObjectId(activity_id)})
        print('Deleting an activity after delete!!')
        if res.deleted_count == 0:
            return jsonify({'errors':[{'msg':'Id doesnot exist'}]}),404
        return jsonify({'msg':'Deleted the activity successfuly!!'}),200
    except Exception as e:
        return jsonify({'errors':[{'msg':'Server Error!!'}]}),500