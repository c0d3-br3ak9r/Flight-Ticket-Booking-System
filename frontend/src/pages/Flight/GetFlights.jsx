import { useEffect, useState } from "react";
import { getCookie } from "../../helpers/validation";
import { DisplayFlight } from "../../components/Flight/DisplayFlight";

export const GetFlights = () => {

    let [flights, setFlights] = useState([]);

    const getFlights = async () => {
        let cookie = getCookie(document.cookie);
        let newflights = [];
        await fetch("/flight", {
            method: "GET",
            headers: {
                "Content-Type": "application/json",
                "id": cookie
            },
        }).then((res) => {
            if ( res.status === 200 ) {
                res.json().then((data) => {
                    data["flights"].forEach(e => {
                        newflights.push(e);
                    })
                    setFlights(newflights);
                })
            }
        });
    }

    useEffect(() => {
        getFlights();
    }, [])

    return (
    <>
    <div className="flex flex-col bg-white border-2 rounded-md p-10 m-10">
        <p className="text-2xl text-bold text-center mb-4">Get Flights</p>
        {flights.map((flight, idx) => 
        <DisplayFlight key={idx} flight_no={flight.flight_no} airline={flight.airline} flight_timing_id={flight.flight_timing_id}
            source={flight.source} destination={flight.destination} date={flight.date} time={flight.time}/>)}
    </div>
    </>
    );
};