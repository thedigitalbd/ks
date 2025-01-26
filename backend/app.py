from flask import Flask, jsonify, request
from config import Config
from models import db, User, ActivityLog

app = Flask(__name__)
app.config.from_object(Config)

# Initialize the database
db.init_app(app)

@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([
        {"id": u.id, "name": u.name, "location": u.location} for u in users
    ])

@app.route('/api/log_activity', methods=['POST'])
def log_activity():
    user_id = request.json.get('user_id')
    activity = request.json.get('activity')

    if not user_id or not activity:
        return jsonify({"error": "Invalid data"}), 400

    new_log = ActivityLog(user_id=user_id, activity=activity)
    db.session.add(new_log)
    db.session.commit()
    return jsonify({"message": "Activity logged successfully"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
    app.run(debug=True)
