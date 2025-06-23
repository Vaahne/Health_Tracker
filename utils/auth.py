import jwt
from datetime import datetime, timedelta
from flask import jsonify,request,current_app,g
from functools import wraps

def generate_token(payload):
    return jwt.encode(
        {"user": payload, "exp": datetime.utcnow() + timedelta(hours=1)},
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("x-auth-token")
        # if "Authorization" in request.headers:
        #     try:
        #         token = request.headers["Authorization"].split(" ")[1]
        #     except:
        #         return jsonify({"errors": [{"msg": "Invalid token format"}]}), 403

        if not token:
            return jsonify({"errors": [{"msg": "Token is missing"}]}), 403

        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            g.user = data["user"]
        except jwt.ExpiredSignatureError:
            return jsonify({"errors": [{"msg": "Token expired"}]}), 401
        except jwt.InvalidTokenError:
            return jsonify({"errors": [{"msg": "Invalid token"}]}), 401

        return f(*args, **kwargs)
    return decorated