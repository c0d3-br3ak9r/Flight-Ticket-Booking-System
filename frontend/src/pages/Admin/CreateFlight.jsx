import { useRef } from "react";

export const CreateFlight = () => {
    const flightNoRef = useRef();

    return (
    <>
        <div className="flex flex-col bg-white border-2 rounded-md p-10 m-10">
            <p className="text-2xl text-bold text-center">Add Flight</p>

            <p className="text-xl mt-8">Flight No</p>
            <input ref={flightNoRef} type="text" placeholder="Username goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" />

            <p className="text-xl mt-8">Source</p>
            <input ref={flightNoRef} type="text" placeholder="Username goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" />

            <p className="text-xl mt-8">Destination</p>
            <input ref={flightNoRef} type="text" placeholder="Username goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" />

            <p className="text-xl mt-8">Airline</p>
            <input ref={flightNoRef} type="text" placeholder="Username goes here..." className="p-4 mt-4 w-full h-10 border-4 rounded-lg focus:outline-none focus:ring focus:border-green-500" />
        </div>
    </>
    );
}