import { useRef } from "react";
import { getCookie } from '../../helpers/validation';

export const CreateFlight = () => {
    const flightNoRef = useRef();
    const airlineRef = useRef();
    const sourceRef = useRef();
    const destinationRef = useRef();
    const firstClassRef = useRef();
    const businessClassRef = useRef();
    const economyClassRef = useRef();



    const callCreate = async () => {
        let cookie = getCookie(document.cookie);
        
        await fetch("/flight", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "id": cookie
            },
            body: JSON.stringify({
                flight_no: flightNoRef.current.value,
                destination: destinationRef.current.value,
                source: sourceRef.current.value,
                airline: airlineRef.current.value,
                first_class_seat: firstClassRef.current.value,
                business_class_seat: businessClassRef.current.value,
                economy_class_seat: economyClassRef.current.value,
            }),
        }).then((res) => {
            if ( res.status === 200 ) {
                alert("Success");
            } else {
                alert("Failed");
            }
        });
    }

    return (
    <>
        <div className="flex flex-col bg-white border-2 rounded-md p-10 m-10">
            <p className="text-2xl text-bold text-center">Add Flight</p>

            <p className="text-xl mt-8">Flight No</p>
            <input ref={flightNoRef} type="text" placeholder="Flight No goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" />

            <p className="text-xl mt-8">Source</p>
            <input ref={sourceRef} type="text" placeholder="Source goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>

            <p className="text-xl mt-8">Destination</p>
            <input ref={destinationRef} type="text" placeholder="Destination goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>

            <p className="text-xl mt-8">Airline</p>
            <input ref={airlineRef} type="text" placeholder="Airline goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>

            <p className="text-xl mt-8">No of Seats in First class</p>
            <input ref={firstClassRef} type="number" placeholder="First class seat count goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>

            <p className="text-xl mt-8">No of Seats in Business class</p>
            <input ref={businessClassRef} type="number" placeholder="Business class seat count goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>

            <p className="text-xl mt-8">No of Seats in Economy class</p>
            <input ref={economyClassRef} type="number" placeholder="Economy class seat count goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" required/>

            <div className="flex justify-center items-center flex-col">
                <button onClick={callCreate} className="text-xl w-24 h-10 bg-[#85ffff] hover:bg-[#85ffa5] rounded-md mt-4">Submit</button>
            </div>
        </div>
    </>
    );
}