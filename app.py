from flask import jsonify, Flask , request
# from routes.userRoutes import userRouter
# from routes.goalRoutes import goalRouter
# from models.Activities import activities
from routes.activityRoutes import activityRouter
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# app.register_blueprint(userRouter, url_prefix="/api/users")
# app.register_blueprint(goalRouter, url_prefix="/api/goals")
app.register_blueprint(activityRouter,url_prefix="/api/activities")

if __name__ == "__main__":
    app.run(debug=True)