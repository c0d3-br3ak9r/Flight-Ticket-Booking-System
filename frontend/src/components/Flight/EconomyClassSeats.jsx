import { Seat } from "./Seat";

export const EconomyClassSeats = ({economyClass, toggleSeat}) => {
    return (
        <>
        <div className="flex flex-row">
            <div className="grid grid-cols-11 gap-x-3">
                {economyClass.map((s, idx) => 
                {return ( <Seat cls='E' key={idx} seat={s.seat} booked={s.booked} selected={s.selected}
                toggleSeat={toggleSeat} isLast={idx%3===2 && idx%8!==0}/> ) 
                })}
            </div>
        </div>
        </>
        );
}