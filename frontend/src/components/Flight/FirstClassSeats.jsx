import { Seat } from "./Seat";

export const FirstClassSeats = ({firstClass}) => {
    return (
    <>
    <div className="flex flex-row">
        <div className="grid grid-cols-5 gap-x-1">
            {firstClass.map((s, idx) => 
            {return ( <Seat seat={s.seat} booked={s.booked} isLast={idx%2==1 && idx%4==1}/> ) 
            })}
        </div>
    </div>
    </>
    );
}