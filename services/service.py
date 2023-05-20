from services import session
from services.admin import admin
from services.flight import flight

def remove_flight(session_id, flight_no):
    if ( session_id and admin.validate_session(session_id) ):
        if ( str.isalnum(flight_no) ):
            return flight.remove_flight(flight_no)
        return 2
    return 4