import { GetSeatMapping } from "./GetSeatMapping";
import { useLocation } from "react-router-dom";
import { getCookie, validateCookie } from "../../helpers/validation";
import { useEffect, useState } from "react";

export const GetFlightDetails = () => {
    const location = useLocation();

    let [flightDetails, setFlightDetails] = useState({});

    const getDetails = async () => {
        let cookie = getCookie(document.cookie);
        await fetch("/flight-details", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "id": cookie
            },
            body: JSON.stringify({
                flight_timing_id: location.state.flight_timing_id,
            })
        }).then((res) => {
            if ( res.status === 200 ) {
                res.json().then((data) => {
                    console.log(data);
                    setFlightDetails(data);
                })
            }
        });
    }

    const display = (data) => {
        
    }

    useEffect(() => {
        (async () => {
            if ( !(await validateCookie(document.cookie, "user")) ) {
                window.open("/login", "_self");
           }
           getDetails();
        })();
    }, [])

    return (
    <>
    <div>
        <p>{flightDetails.flight_no  }</p>
        <GetSeatMapping bookedSeats={flightDetails.booked_seats} firstClassCount={flightDetails.first_class_seat}
        businessClassCount={flightDetails.business_class_seat} economyClassCount={flightDetails.economy_class_seat}/>
    </div>
    </>
    );
};