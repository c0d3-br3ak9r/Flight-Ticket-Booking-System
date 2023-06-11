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
        <div className="flex justify-center items-center flex-col m-auto h-screen bg-[#e8e6e6] border">
        <div className="p-10 sm:w-1/2 lg:w-2/5 h-auto flex justify-center flex-col m-auto h-screen bg-[#e8e6e6aa] border">
            <p className="text-3xl text-center font-bold mt-8">Admin Login</p>

            <p className="text-xl mt-8">Username</p>
            <input ref={usernameRef} type="text" placeholder="Username goes here..." className="p-4 mt-4 w-full h-10 border-1 rounded-20 focus:outline-none focus:ring focus:border-green-500" />

            <p className="text-xl mt-8">Password</p>
            <input ref={passwordRef} type="password" placeholder="Password goes here..." className="p-4 mt-4 w-full h-10 border-1 rounded-20 focus:outline-none focus:ring focus:border-green-500" />

            <div className="flex justify-center">
                <p className="text-red-500">{info}</p>
                <button onClick={login} className="text-xl w-24 h-10 bg-[#85ffff] hover:bg-[#85ffa5] rounded-md mt-8">Submit</button>
            </div>
        </div>
        </div>
    </>
    );
};
