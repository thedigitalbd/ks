from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from routes import auth_bp, users_bp

# Initialize app
app = Flask(__name__)

# App configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://neondb_owner:npg_QWYXOSC3JhM9@ep-red-moon-a83h1tud-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
app.config['SECRET_KEY'] = "5fc6d8ab661706f61c16e1ddcf98a2778e259ec37b891e58d8b26e8ab8bf0d39af80844883ab5d63f5970741d5e2076efd3de1649acb47123daaa11f277332a1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Register blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(users_bp, url_prefix='/users')

if __name__ == "__main__":
    app.run()
