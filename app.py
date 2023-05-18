from flask import Flask, request
from services import admin, session

app = Flask(__name__)

# To load environment variables
app.config.from_pyfile('settings.py')

@app.route('/')
def index():
    return "Hello, World!"

# Admin password - cb!NmgQ07eX5
''' To authenticate admin user '''
@app.route('/admin/login')
def admin_login():
    username = request.json["username"]
    password = request.json["password"]
    res = admin.is_valid_user(username, password)
    if res:
        session.create_admin_session(res)
        return "Success"
    return "Failed"

app.run(debug=True)