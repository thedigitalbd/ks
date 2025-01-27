from flask import jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from models import db, User
from . import auth_bp
from werkzeug.security import check_password_hash

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password_hash, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Invalid credentials"}), 401
