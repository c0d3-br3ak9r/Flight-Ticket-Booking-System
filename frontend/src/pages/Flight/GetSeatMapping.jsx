import { FirstClassSeats } from "../../components/Flight/FirstClassSeats";
import { BusinessClassSeats } from "../../components/Flight/BusinessClassSeats";
import { EconomyClassSeats } from "../../components/Flight/EconomyClassSeats";

export const GetSeatMapping = () => {

    const seatMap = {
        firstClass : [
            {seat : "F1", booked: false}, {seat : "F2", booked: false},
            {seat : "F3", booked: true}, {seat : "F4", booked: false},
            {seat : "F5", booked: false}, {seat : "F6", booked: true},
            {seat : "F7", booked: false}, {seat : "F8", booked: false}
        ],
        businessClass : [
            {seat : "B1", booked: false}, {seat : "B2", booked: false},
            {seat : "B3", booked: true}, {seat : "B4", booked: false},
            {seat : "B5", booked: false}, {seat : "B6", booked: true},
            {seat : "B7", booked: false}, {seat : "B8", booked: false},
            {seat : "B9", booked: false}, {seat : "B10", booked: false},
            {seat : "B11", booked: false}, {seat : "B12", booked: false}
        ],
        economyClass : [
            {seat : "E1", booked: false}, {seat : "E2", booked: false},
            {seat : "E3", booked: true}, {seat : "E4", booked: false},
            {seat : "E5", booked: false}, {seat : "E6", booked: true},
            {seat : "E7", booked: false}, {seat : "E8", booked: false},
            {seat : "E9", booked: false}, {seat : "E10", booked: false},
            {seat : "E11", booked: false}, {seat : "E12", booked: false}
        ]
    }

    return (
    <>
    <div className="flex flex-col items-center">
        <p className="m-4">First Class Seats</p>
        <FirstClassSeats firstClass={seatMap.firstClass}/>
        <p className="m-4">Business Class Seats</p>
        <BusinessClassSeats businessClass={seatMap.businessClass}/>
        <p className="m-4">Economy Class Seats</p>
        <EconomyClassSeats economyClass={seatMap.economyClass}/>
    </div>
    </>
    );
};