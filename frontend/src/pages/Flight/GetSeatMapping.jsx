import { useState } from "react";
import { FirstClassSeats } from "../../components/Flight/FirstClassSeats";
import { BusinessClassSeats } from "../../components/Flight/BusinessClassSeats";
import { EconomyClassSeats } from "../../components/Flight/EconomyClassSeats";


export const GetSeatMapping = ({bookedSeats, firstClassCount, businessClassCount, economyClassCount}) => {

    const getSeats = (cls, count) => {
        let seats = [];
        for (let i=1; i<=count; i++ ) {
            seats.push({
                seat: cls + i,
                booked: bookedSeats.includes(cls+i),
                selected: false
            });
        }
        return seats;
    }

    const [firstClass, setFirstClass] = useState(getSeats('F', firstClassCount));
    const [businessClass, setBusinessClass] = useState(getSeats('B', businessClassCount));
    const [economyClass, setEconomyClass] = useState(getSeats('E', economyClassCount));

    const toggleSeat = (seat, cls) => {
        const newSeats = cls === 'F' ? [...firstClass] : 
                                    cls === 'B' ? [...businessClass] : [...economyClass];
        const newSeat = newSeats.find((s) => s.seat === seat);
        newSeat.selected = !newSeat.selected;
        cls === 'F' ? setFirstClass(newSeats) :
                      cls === 'B' ? setBusinessClass(newSeats) : setEconomyClass(newSeats);
        console.log(newSeats);
    }

    return (
    <>
    <div className="flex flex-col items-center">
        <p className="m-4">First Class Seats</p>
        <FirstClassSeats firstClass={firstClass} toggleSeat={toggleSeat}/>
        <p className="m-4">Business Class Seats</p>
        <BusinessClassSeats businessClass={businessClass} toggleSeat={toggleSeat}/>
        <p className="m-4">Economy Class Seats</p>
        <EconomyClassSeats economyClass={economyClass} toggleSeat={toggleSeat} />
    </div>
    </>
    );
};