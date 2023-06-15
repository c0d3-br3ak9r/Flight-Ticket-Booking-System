export const Seat = ({seat, cls, booked, isLast, toggleSeat, selected}) => {
    const baseCSS = "p-2 m-1 w-10 h-10 text-center rounded-md border-2 text-center flex items-center justify-center ";

    const handleTodo = () => {
        toggleSeat(seat, cls)
    }

    return (
        <>
        <div className={ (booked ? baseCSS + "bg-[#ffaaaa] hover:bg-[#ff7777]" :
                                    (selected ? baseCSS + "bg-[#aaffaa] hover:bg-[#77ff77]" : baseCSS + "hover:bg-[#77ff77]" ))}
                onClick={handleTodo}>
            {seat}
        </div>
        {isLast ? <div className="baseCSS"></div> : <></>}
        </>
    );
}