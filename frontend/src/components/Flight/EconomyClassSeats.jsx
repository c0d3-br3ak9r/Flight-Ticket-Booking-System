import { Seat } from "./Seat";

export const EconomyClassSeats = ({economyClass}) => {
    return (
        <>
        <div className="flex flex-row">
            <div className="grid grid-cols-11 gap-x-3">
                {economyClass.map((s, idx) => 
                {return ( <Seat seat={s.seat} booked={s.booked} isLast={idx%3==2 && idx%8!=0}/> ) 
                })}
            </div>
        </div>
        </>
        );
}