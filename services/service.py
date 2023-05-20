from services import session, validation
from services.admin import admin
from services.flight import flight

''' To remove a flight '''
def remove_flight(session_id, flight_no):
    if ( session_id and admin.validate_session(session_id) ):
        if ( str.isalnum(flight_no) ):
            return flight.remove_flight(flight_no)
        return 2
    return 4


''' To remove a flight timing '''
def remove_flight_timing(session_id, flight_no, date, time):
    if ( session_id and admin.validate_session(session_id) ):
        if ( ( flight_no and str.isalnum(flight_no) ) or 
                ( date and validation.is_valid_date(date) ) or 
                ( time and validation.is_valid_time(time) ) ):
            return flight.remove_flight_timing(flight_no, date, time)
    return 4