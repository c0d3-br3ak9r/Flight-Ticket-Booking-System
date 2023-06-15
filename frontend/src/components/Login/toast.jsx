import { useRef } from "react";

export const Toast = (msg) => {

    const toastRef = useRef();

    return (
    <>
    <div ref={toastRef} className="">
        <p>{msg}</p>
    </div>
    </>
    );
}