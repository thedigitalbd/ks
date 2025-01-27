from flask import jsonify, request
from flask_jwt_extended import jwt_required
from models import db, User
from . import users_bp

@users_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    users = User.query.all()
    users_data = [{"id": u.id, "username": u.username, "role": u.role} for u in users]
    return jsonify(users_data), 200
