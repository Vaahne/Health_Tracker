from flask import jsonify, Flask , request
from config import collection

app = Flask(__name__)

@app.route('/add',methods=['POST'])
def add_user():
    data = request.json
    collection.insert_one(data)
    return jsonify({'message': 'User added!'})

@app.route('/users'.methods=['GET'])
def get_users():
    users = list(collection.find({},{_id:0})) # Excluding mongodb _ids
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)