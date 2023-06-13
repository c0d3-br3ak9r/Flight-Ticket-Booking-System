import { useEffect, useRef, useState } from "react";
import { getCookie } from '../../helpers/validation';

export const AddFlightTiming = () => {
    const flightNoRef = useRef();
    let [flights, setFlights] = useState([]);

    const getFlights = async () => {
        let cookie = getCookie(document.cookie);
        let newflights = [];
        await fetch("/created-flights", {
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
        <p className="text-2xl text-bold text-center">Add Flight Timing</p>

        <p className="text-xl mt-8">Flight No</p>
        <input ref={flightNoRef} type="text" placeholder="Username goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" />

        <p className="text-xl mt-8">Date</p>
        <input ref={flightNoRef} type="date" placeholder="Username goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" />

        <p className="text-xl mt-8">Time</p>
        <input ref={flightNoRef} type="time" placeholder="Username goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" />

        <p className="text-xl mt-8">Airline</p>
        <select name="airline" className="mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500">
            <option value="">--Select an airline--</option>
            {(!flights.length) ? <option>Loading...</option> : flights.map((flight, idx) => <option key={idx} value={flight}>{flight}</option>)}
        </select>
    </div>
    </>
    );
};