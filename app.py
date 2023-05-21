from flask import Flask, request
from services import service


app = Flask(__name__)


@app.route('/')
def index():
    return ("Flight Ticket Booking System!", 200)


''' To create a new admin user '''
@app.route('/admin/signup', methods=["POST"])
def create_admin():
    resp = service.create_admin(request.json)
    return get_response(resp)


# Admin username - admin_user
# Admin password - cb!NmgQ07eX5
''' To authenticate admin user '''
@app.route('/admin/login', methods=["POST"])
def admin_login():
    resp = service.authenticate_admin(request.json)
    return get_response(resp)


''' To create a new flight '''
@app.route('/flight', methods=["POST"])
def create_flight():
    resp = service.create_flight(request.headers.get("id"), request.json)
    return get_response(resp)


''' To add flight timing for already created flight '''
@app.route('/flight-timing', methods=["POST"])
def create_flight_timing():
    resp = service.create_flight_timing(request.headers.get("id"), request.json)
    return get_response(resp)


''' To remove a flight '''
@app.route('/flight', methods=["DELETE"])
def remove_flight():
    resp = service.remove_flight(request.headers.get("id"), request.json)
    return get_response(resp)


''' To remove a flight timing '''
@app.route('/flight-timing', methods=["DELETE"])
def remove_flight_timing():
    resp = service.remove_flight_timing(request.headers.get('id'), request.json)
    return get_response(resp)


''' To get all bookings '''
@app.route('/bookings', methods=["GET"])
def get_all_bookings():
    resp = service.get_all_bookings(request.headers.get('id'), request.json)
    return get_response(resp)


''' To logout admin '''
@app.route('/admin/logout', methods=["POST"])
def logout_admin():
    resp = service.logout_admin(request.headers.get('id'))
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