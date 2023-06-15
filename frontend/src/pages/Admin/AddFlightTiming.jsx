import { useEffect, useRef, useState } from "react";
import { getCookie } from '../../helpers/validation';

export const AddFlightTiming = () => {
    const flightNoRef = useRef();
    const dateRef = useRef();
    const timeRef = useRef();
    const firstClassRef = useRef();
    const businessClassRef = useRef();
    const economyClassRef = useRef();

    let [flights, setFlights] = useState([]);


    const callCreate = async () => {
        let cookie = getCookie(document.cookie);
        
        await fetch("/flight-timing", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "id": cookie
            },
            body: JSON.stringify({
                flight_no: flightNoRef.current.value,
                date: dateRef.current.value,
                time: timeRef.current.value,
                first_class_price: firstClassRef.current.value,
                business_class_price: businessClassRef.current.value,
                economy_class_price: economyClassRef.current.value,
            }),
        }).then((res) => {
            if ( res.status === 200 ) {
                alert("Success");
            } else {
                alert("Failed");
            }
        });
    }


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
        <select ref={flightNoRef} name="airline" className="mt-4 pl-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required>
            <option value="">--Select an flight--</option>
            {(!flights.length) ? <option>Loading...</option> : flights.map((flight, idx) => <option key={idx} value={flight}>{flight}</option>)}
        </select>

        <p className="text-xl mt-8">Date</p>
        <input ref={dateRef} type="date" placeholder="Date goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>

        <p className="text-xl mt-8">Time</p>
        <input ref={timeRef} type="time" placeholder="Time goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>

        <p className="text-xl mt-8">First Class Ticket Price</p>
        <input ref={firstClassRef} type="number" placeholder="First Class Ticket Price goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>

        <p className="text-xl mt-8">Business Class Ticket Price</p>
        <input ref={businessClassRef} type="number" placeholder="Business Class Ticket Price goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>

        <p className="text-xl mt-8">Economy Class Ticket Price</p>
        <input ref={economyClassRef} type="number" placeholder="Economy Class Ticket Price goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>
        
        <div className="flex justify-center items-center flex-col">
            <button onClick={callCreate} className="text-xl w-24 h-10 bg-[#85ffff] hover:bg-[#85ffa5] rounded-md mt-4">Submit</button>
        </div>
    </div>
    </>
    );
};