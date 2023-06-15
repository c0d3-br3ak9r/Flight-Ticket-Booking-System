import { Seat } from "./Seat";

export const BusinessClassSeats = ({businessClass, toggleSeat}) => {
    return (
        <>
        <div className="flex flex-row">
            <div className="grid grid-cols-11 gap-x-3">
                {businessClass.map((s, idx) => 
                {return ( <Seat key={idx} cls='B' seat={s.seat} booked={s.booked} toggleSeat={toggleSeat}
                selected={s.selected} isLast={idx%3===2 && idx%8!==0}/> ) 
                })}
            </div>
        </div>
        </>
        );
}