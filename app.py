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
    resp = service.create_flight(request.headers.get("id"),
                                request.json.get("flight_no"),
                                request.json.get("airline"), 
                                request.json.get("source"),
                                request.json.get("destination"))
    return get_response(resp)


''' To add flight timing for already created flight '''
@app.route('/flight-timing', methods=["POST"])
def create_flight_timing():
    resp = service.create_flight_timing(request.headers.get("id"),
                                        request.json.get("flight_no"),
                                        request.json.get("date"), 
                                        request.json.get("time"))
    return get_response(resp)


''' To remove a flight '''
@app.route('/flight', methods=["DELETE"])
def remove_flight():
    resp = service.remove_flight(request.headers.get("id"), request.json.get("flight_no"))
    return get_response(resp)


''' To remove a flight timing '''
@app.route('/flight-timing', methods=["DELETE"])
def remove_flight_timing():
    resp = service.remove_flight_timing(request.headers.get('id'),
                                        request.json.get('flight_no'), request.json.get('date'), 
                                        request.json.get('time'))
    return get_response(resp)


''' To get all bookings '''
@app.route('/bookings', methods=["GET"])
def get_all_bookings():
    resp = service.get_all_bookings(request.headers.get('id'),
                                    request.json.get('flight_no'), request.json.get('date'), 
                                    request.json.get('time'))
    return get_response(resp)


''' To create a new user '''
@app.route('/signup', methods=["POST"])
def create_user():
    resp = service.create_user(request.json)
    return get_response(resp)


''' To authenticate a user '''
@app.route('/login', methods=["POST"])
def login_user():
    resp = service.authenticate_user(request.json)
    return get_response(resp)


''' To get available flights based on date and time '''
@app.route('/flight', methods=["GET"])
def get_flights():
    resp = service.get_flights(request.headers.get('id'), request.json)
    return get_response(resp)


''' To book flight ticket '''
@app.route('/book-ticket', methods=["POST"])
def book_ticket():
    resp = service.book_flight(request.headers.get('id'), request.json)
    return get_response(resp)


''' To get all bookings made by user '''
@app.route('/my-bookings', methods=["GET"])
def get_bookings():
    resp = service.get_bookings(request.headers.get('id'))
    return get_response(resp)


''' To logout user '''
@app.route('/logout', methods=["POST"])
def logout_user():
    resp = service.logout_user(request.headers.get('id'))
    return get_response(resp)


def get_response(resp):
    match resp:
        case 1: return ("Success", 200)
        case 2: return ("Bad request", 400)
        case 3: return ("Database error", 500)
        case 4: return ("Forbidden", 403)
        case _: return resp


app.run(debug=True)