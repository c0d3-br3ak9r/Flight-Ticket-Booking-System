export const Seat = ({seat, booked, isLast}) => {
    const baseCSS = "p-2 m-1 w-10 h-10 text-center rounded-md ";
    return (
        <>
        <div className={ baseCSS + (booked ? "bg-[#ffaaaa] hover:bg-[#ffcccc]" : "bg-[#aaffaa] hover:bg-[#ccffcc]")}>
            {seat}
        </div>
        {isLast ? <div className="baseCSS"></div> : <></>}
        </>
    );
}