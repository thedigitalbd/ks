from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
users_bp = Blueprint('users', __name__, url_prefix='/users')

from . import auth, users
