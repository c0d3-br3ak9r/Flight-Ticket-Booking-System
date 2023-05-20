from flask import Flask, request
from services import session, service
from services.admin import admin
from services.flight import flight


app = Flask(__name__)


# To load environment variables
app.config.from_pyfile('settings.py')

@app.route('/')
def index():
    return ("Hello, World!", 200)


# Admin password - cb!NmgQ07eX5
''' To authenticate admin user '''
@app.route('/admin/login', methods=["POST"])
def admin_login():
    username = request.json["username"]
    password = request.json["password"]
    res = admin.is_valid_user(username, password)
    if res:
        if ( session.create_admin_session(res) ):
            return "Success", 200
    return "Failed", 401


''' To create a new flight '''
@app.route('/flight', methods=["POST"])
def create_flight():
    if ( admin.validate_session(request.headers.get("id")) ):
        payload = request.json
        return flight.create_flight(payload["flight_no"], payload["airline"],
                                    payload["source"], payload["destination"])
    return "Forbidden", 403


''' To add flight timing for already created flight '''
@app.route('/flight-timing', methods=["POST"])
def create_flight_timing():
    if ( admin.validate_session(request.headers.get("id")) ):
        payload = request.json
        return flight.create_flight_timing(payload["flight_no"], payload["date"],
                                            payload["time"])
    return "Forbidden", 403


''' To remove a flight timing '''
@app.route('/flight', methods=["DELETE"])
def remove_flight():
    resp = service.remove_flight(request.headers.get("id"), request.json["flight_no"])
    match resp:
        case 1: return ("Success", 200)
        case 2: return ("Bad request", 400)
        case 3: return ("Database error", 500)
        case 4: return ("Forbidden", 403)
app.run(debug=True)