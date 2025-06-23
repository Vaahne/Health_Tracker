from flask import jsonify, Flask , request
from routes.userRoutes import userRouter
from routes.goalRoutes import goalRouter
from routes.activityRoutes import activityRouter
from routes.activityTrackerRoutes import activityTrackerRouter
from flask_cors import CORS
from config import SECRET_KEY

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY  # getting the secret key from config.py

CORS(app)  # for connecting to the frontend

app.register_blueprint(userRouter, url_prefix="/api/users") # for user Routes 
app.register_blueprint(goalRouter, url_prefix="/api/goals") # for goal Routes
app.register_blueprint(activityRouter,url_prefix="/api/activities") # for activity Routes
app.register_blueprint(activityTrackerRouter,url_prefix="/api/activitytracker") # for Activity tracker routes

if __name__ == "__main__":
    app.run(debug=True)