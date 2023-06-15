import { useEffect, useState } from "react";
import { getCookie } from '../../helpers/validation';

export const DeleteFlight = () => {
    let [flights, setFlights] = useState([]);


    const callDelete = async () => {
        let cookie = getCookie(document.cookie);
        let targetFlights = [];
        flights.forEach((flight) => {
            if ( flight.remove )
                targetFlights.push(flight.name);
        });
        
        await fetch("/flight", {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",
                "id": cookie
            },
            body: JSON.stringify({
                flights: targetFlights
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
                        newflights.push({name: e, remove: false});
                    })
                    setFlights(newflights);
                })
            }
        });
    }

    const toggleCheck = (tmp) => {
        const flightName = tmp.target.name
        let data = [...flights];
        const newFlights = data.find(flight => flight.name === flightName);
        newFlights.remove = !newFlights.remove;
        setFlights(data)
    }

    useEffect(() => {
        getFlights();
    }, [])

    return (
    <>
    <div className="flex flex-col bg-white border-2 rounded-md p-10 m-10">
    <p className="text-2xl text-bold text-center">Delete Flight</p>

    <p className="text-xl mt-8">Choose flights to be removed</p>
        {flights.map((flight, idx) => 
        {return (<label className="m-2 mt-4">
            <input type="checkbox" key={idx} name={flight.name} id={flight.name} onChange={toggleCheck} checked={flight.remove} className="mr-4"/>
            {flight.name}
        </label>)})}

        <div className="flex justify-center items-center flex-col">
            <button onClick={callDelete} className="text-xl w-24 h-10 bg-[#85ffff] hover:bg-[#85ffa5] rounded-md mt-4">Submit</button>
        </div>
    </div>
    </>);
};