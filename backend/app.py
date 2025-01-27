from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_swagger_ui import get_swaggerui_blueprint
from routes import auth_bp, users_bp
from config import Config

# Initialize app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)

# Swagger UI setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "KS API"})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
