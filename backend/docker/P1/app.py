from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Update the URI to match the credentials and service name from docker-compose.yml
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://myuser:mypassword@mysql/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Endpoint to get all users
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'message': 'Healthy'}), 200

# Endpoint to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users_list = User.query.all()
    users = []
    for user in users_list:
        users.append({"id": user.id, "username": user.username, "email": user.email})
    return jsonify(users)

# Endpoint to add a new user
@app.route('/user', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)