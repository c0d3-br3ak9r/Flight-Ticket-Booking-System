import { useRef, useState } from "react";
import { json } from "react-router-dom";

export const AdminSignup = () => {
    const usernameRef = useRef();
    const passwordRef = useRef();
    const cPasswordRef = useRef();
    const [info, setInfo] = useState("");

    const login = () => {
        const username = usernameRef.current.value;
        const password = passwordRef.current.value;
        const cPassword = cPasswordRef.current.value;

        const data = {
            username, password
        }

        if ( password === cPassword ) {
            fetch("/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            }).then((res) => {
                if ( res.status === 200 ) {
                    window.open('/admin/signup', "_self");
                } else if ( res.status === 400 ) {
                    setInfo("Invalid username or password");
                } else if ( res.status === 500 ) {
                    setInfo("Contact admin");
                } else if ( res.status === 403 ) {
                    window.open('/login', "_self");
                }
            });
        }
    };

    return (
    <>
        <div className="flex justify-center items-center flex-col m-auto h-screen bg-[#05ad32] border">
            <p className="text-3xl font-bold">Admin Signup</p>
            <div className="w-1/2 flex flex-row justify-evenly mt-8">
                <p className="text-xl">Username</p>
                <input ref={usernameRef} type="text" className="w-60 h-10 border-4 rounded-md focus:outline-none focus:ring focus:border-green-500" />
            </div>
            <div className="w-1/2 flex flex-row justify-evenly mt-8">
                <p className="text-xl">Password</p>
                <input ref={passwordRef} type="text" className="w-60 h-10 border-4 rounded-md focus:outline-none focus:ring focus:border-green-500" />
            </div>
            <span title="Hiii">i</span>
            <div className="w-1/2 flex flex-row justify-evenly mt-8">
                <p className="text-xl">Confirm Password</p>
                <input ref={cPasswordRef} type="text" className="w-60 h-10 border-4 rounded-md focus:outline-none focus:ring focus:border-green-500" />
            </div>
            <p className="text-red-500">{info}</p>
            <button onClick={login} className="w-20 h-8 bg-[#85ffa5] rounded-md mt-8">Submit</button>
        </div>
    </>
    );
};
