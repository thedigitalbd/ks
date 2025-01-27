from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from config import Config
from models import db, User, ActivityLog

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists"}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"})

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"username": username})
    return jsonify({"access_token": access_token})

@app.route('/log_activity', methods=['POST'])
@jwt_required()
def log_activity():
    data = request.json
    user_id = data.get('user_id')
    activity = data.get('activity')

    new_log = ActivityLog(user_id=user_id, activity=activity)
    db.session.add(new_log)
    db.session.commit()
    return jsonify({"message": "Activity logged successfully"})
