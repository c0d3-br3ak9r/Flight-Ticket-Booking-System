# Flight-Ticket-Booking-System
   Flight ticket booking system is a simple CRUD application which has its backend implemented using Flask. 
    It has two users admin and normal user. Admin has the access to add flights, flight timings, delete flights, 
    flight timings and view all bookings. Users can signup, search for flights and book them.
    
## Usage

  1. Clone the repository
      ```
      git clone https://github.com/c0d3-br3ak9r/Flight-Ticket-Booking-System.git
      ```
  2. Install the requirements
      ```
      pip install -r requirements.txt
      ```
  3. Run the app.py file
      ```
      python app.py
      ```

## Endpoints
### Admin Endpoints

  1. Create an admin account
      ```
      POST /admin/signup
      ```
      Pass json in the format:
      ```
      {
        "username" : "admin",
        "password" : "Admin_password123"
      }
      ```
  2. Login as admin
      ```
      POST /admin/login
      ```
      Pass json in the format:
      ```
      {
        "username" : "admin",
        "password" : "Admin_password123"
      }
      ```
      This gives a session id as response. Include the session id in the header for all below endpoints.
      ```
      curl -H "id: $SESSION_ID" /bookings
      ```
  3. Add flights
      ```
      POST /flight
      ```
      Pass json in the format:
      ```
      {
        "flight_no" : "CN666",
        "airline" : "Air Asia",
        "source" : "Chennai",
        "destination" : "Beijing"
      }
      ```
  4. Add flight timings
      ```
      POST /flight-timing
      ```
      Pass json in the format:
      ```
      {
        "flight_no" : "US987",
        "date" : "2023-05-29",
        "time" : "17:10:23"
      }
      ```
  5. Remove flights
      ```
      DELETE /flight
      ```
      Pass json in the format:
      ```
      {
        "flight_no" : "AUS3468"
      }
      ```
  6. Remove flight timings
      ```
      DELETE /flight-timing
      ```
      Pass json in the format:
      ```
      {
        "flight_no" : "US987",
        "date" : "2023-05-29",
        "time" : "17:10:23"
      }
      ```
  7. View all bookings
      ```
      GET /bookings
      ```
      To get specific booking details, pass the json in the format
      ```
      {
        "flight_no" : "US987",
        "date" : "2023-05-29",
        "time" : "17:10:23"
      }
      ```
  8. Admin logout
      ```
      POST /admin/logout
      ```

### User Endpoints
  1. Create a user account
      ```
      POST /signup
      ```
      Pass json in the format:
      ```
      {
        "username" : "user",
        "password" : "User_password123"
      }
      ```
  2. Login as user
      ```
      POST /login
      ```
      Pass json in the format:
      ```
      {
        "username" : "user",
        "password" : "User_password123"
      }
      ```
      This gives a session id as response. Include the session id in the header for all below endpoints.
      ```
      curl -H "id: $SESSION_ID" /bookings
      ```
  3. Search for flights
      ```
      GET /flight
      ```
      Pass json in the format:
      ```
      {
        "flight_no": "US987",
        "date" : "2023-05-29",
        "time": "16:10:23"
      }
      ```
  4. Book a flight ticket
      ```
      POST /book-ticket
      ```
      Pass json in the format:
      ```
      {
        "flight_no": "US987",
        "date" : "2023-05-29",
        "time": "16:10:23"
      }
      ```
  5. View bookings
      ```
      GET /my-bookings
      ```
  6. Logout
      ```
      POST /logout
      ```
      
### HTTP Status Codes Used
   1. 200 - denotes succcessful request.
   2. 400 - denotes invalid input. If you get this, verify whether the passed json is in the correct format.
   3. 500 - Internal error such as in database. Usually occurs if you try to violate constraints such as creating multiple users with same username.
   4. 403 - Not authorized. If you get this, check whether you are authenticated and you are passing session id as said above.
