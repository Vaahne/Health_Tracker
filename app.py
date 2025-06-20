from flask import jsonify, Flask , request
from routes.userRoutes import userRouter
from routes.goalRoutes import goalRouter
from routes.activityRoutes import activityRouter
from routes.activityTrackerRoutes import activityTrackerRouter
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(userRouter, url_prefix="/api/users")
app.register_blueprint(goalRouter, url_prefix="/api/goals")
app.register_blueprint(activityRouter,url_prefix="/api/activities")
app.register_blueprint(activityTrackerRouter,url_prefix="/api/activitytracker")

if __name__ == "__main__":
    app.run(debug=True)