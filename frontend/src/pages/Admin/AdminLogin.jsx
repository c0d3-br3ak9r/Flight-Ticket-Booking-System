import { useRef, useState } from "react";

export const AdminLogin = () => {
    const usernameRef = useRef();
    const passwordRef = useRef();
    const [info, setInfo] = useState("");

    const login = () => {
        const username = usernameRef.current.value;
        const password = passwordRef.current.value;

        const data = {
            username, password
        }

        fetch("/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        }).then((res) => {
            if ( res.status === 200 ) {
                res.json().then((data) => {
                    document.cookie = "id="+ data["session_id"]; //+";secure;HttpOnly";
                })
            } else if ( res.status === 400 ) {
                setInfo("Invalid username or password");
            } else if ( res.status === 500 ) {
                setInfo("Contact admin");
            } else if ( res.status === 403 ) {
                window.open('/login', "_self");
            }
        }
        );
    };

    return (
    <>
        <div className="flex justify-center items-center flex-col m-auto h-screen bg-[#05ad32] border">
            <p className="text-3xl font-bold">Admin Login</p>
            <div className="w-1/2 flex flex-row mt-8">
                <p className="text-xl mr-8">Username</p>
                <input ref={usernameRef} type="text" className="w-60 h-10 border-4 rounded-md focus:outline-none focus:ring focus:border-green-500" />
            </div>
            <div className="w-1/2 flex flex-row mt-8">
                <p className="text-xl mr-8">Password</p>
                <input ref={passwordRef} type="text" className="w-60 h-10 border-4 rounded-md focus:outline-none focus:ring focus:border-green-500" />
            </div>
            <p className="text-red-500">{info}</p>
            <button onClick={login} className="w-20 h-8 bg-[#85ffa5] rounded-md mt-8">Submit</button>
        </div>
    </>
    );
};
