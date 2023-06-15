import { useNavigate } from 'react-router-dom'

export const DisplayFlight = ({flight_no, airline, source, destination, date, time, flight_timing_id}) => {
    const price = 67839;
    const navigate = useNavigate();

    const gotoGetFlightDetails = () => {
        navigate('/get-flight-details', {state:{flight_timing_id}});
    }

    return (
    <>
    <div className="w-full p-4 flex md:flex-row flex-wrap md:flex-nowrap items-center border-2 rounded-md hover:bg-[#f0f0f5]">
        <p className="font-bold text-center basis:1/2 md:basis-1/6">{airline}</p>
        <p className="text-center basis:1/2 md:basis-1/6">{source}</p>
        <div className="flex flex-col mr-4 items-center basis:1/2 md:basis-1/6">
            <p>{date}</p>
            <div className="h-1 w-20 bg-black"></div>
            <p>{time}</p>
        </div>
        <p className="mr-4 basis:1/2 md:basis-1/6 text-center">{destination}</p>
        <div className="basis:1/2 md:basis-1/6 text-center">Starts from <p className="font-bold">₹{price}</p></div>
        <button onClick={()=>gotoGetFlightDetails()} className="basis:1/2 md:basis-1/6 text-xl w-auto h-10 bg-[#85ffff] hover:bg-[#85ffa5] rounded-md mt-4">Book Now</button>
    </div>
    </>
    );
};