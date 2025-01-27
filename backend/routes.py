from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

auth_bp = Blueprint('auth', __name__)
users_bp = Blueprint('users', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    return jsonify(message="Login endpoint")

@auth_bp.route('/register', methods=['POST'])
def register():
    return jsonify(message="Register endpoint")

@users_bp.route('/list', methods=['GET'])
@jwt_required()
def list_users():
    return jsonify(message="List users endpoint")
