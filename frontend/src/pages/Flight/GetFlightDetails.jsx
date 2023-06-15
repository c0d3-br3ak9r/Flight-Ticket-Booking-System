import { GetSeatMapping } from "./GetSeatMapping";
import { useLocation } from "react-router-dom";
import { getCookie, validateCookie } from "../../helpers/validation";
import { useEffect } from "react";

export const GetFlightDetails = () => {
    const location = useLocation();

    let flightDetails;

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
                    flightDetails = data;
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
        <p>{location.state.flight_timing_id  }</p>
        <GetSeatMapping/>
    </div>
    </>
    );
};