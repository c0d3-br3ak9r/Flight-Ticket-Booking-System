import { useRef, useState } from "react";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faInfoCircle } from '@fortawesome/free-solid-svg-icons';
import { validateCookie } from '../../helpers/validation';
import { useEffect } from 'react';

export const AdminSignup = () => {
    const usernameRef = useRef();
    const passwordRef = useRef();
    const cPasswordRef = useRef();
    const [info, setInfo] = useState("");

    const signup = () => {
        const username = usernameRef.current.value;
        const password = passwordRef.current.value;
        const cPassword = cPasswordRef.current.value;

        const data = {
            username, password
        }

        if ( password !== cPassword ) {
            setInfo("Password and Confirm Passwords does not match!")
            return 
        }

        fetch("/admin/signup", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        }).then((res) => {
            if ( res.status === 200 ) {
                window.open('/admin/login', "_self");
            } else if ( res.status === 400 ) {
                setInfo("Invalid username or password");
            } else if ( res.status === 500 ) {
                setInfo("Contact admin");
            } else if ( res.status === 403 ) {
                window.open('/login', "_self");
            }
        });
    };

    const enterEvent = (e) => {
        if ( e.key === "Enter" ) {
            signup();
        }
    };

    useEffect(() => {
        if ( validateCookie(document.cookie, "admin") ) {
            window.open("/admin/dashboard", "_self");
        }
        usernameRef.current.addEventListener("keyup", (e) => enterEvent(e));
        passwordRef.current.addEventListener("keyup", (e) => enterEvent(e));
        cPasswordRef.current.addEventListener("keyup", (e) => enterEvent(e));
    }, [])

    return (
    <>
    <div className="flex justify-center items-center flex-col m-auto h-screen bg-[#e8e6e6] border">
        <div className="p-10 sm:w-1/2 lg:w-2/5 h-auto flex justify-center flex-col m-auto h-screen bg-[#e8e6e6aa] border">
            <p className="text-3xl text-center font-bold mt-8">Admin Signup</p>

            <div className="flex flex-row items-center">
                <p className="text-xl mt-8">Username</p>
                <FontAwesomeIcon className="ml-2 mt-9" icon={faInfoCircle} title="Username must consist of only alphabets, digits and underscore with length between 4 and 20"/>
            </div>            
            <input ref={usernameRef} type="text" placeholder="Username goes here..." className="p-4 mt-4 w-full h-10 border-1 rounded-20 focus:outline-none focus:ring focus:border-green-500" />

            <div className="flex flex-row items-center">
                <p className="text-xl mt-8">Password</p>
                <FontAwesomeIcon className="ml-2 mt-9" icon={faInfoCircle} title="Password must contain of atleast one lowercase alphabet, one uppercase alphabet, one digit and one special character with length between 8 and 20"/>
            </div>
            <input ref={passwordRef} type="password" placeholder="Password goes here..." className="p-4 mt-4 w-full h-10 border-1 rounded-20 focus:outline-none focus:ring focus:border-green-500" />

            <p className="text-xl mt-8">Confirm Password</p>
            <input ref={cPasswordRef} type="password" placeholder="Confirm your password..." className="p-4 mt-4 w-full h-10 border-1 rounded-20 focus:outline-none focus:ring focus:border-green-500" />

            <div className="flex justify-center items-center flex-col">
                <p className="text-red-500 mt-4 text-center">{info}</p>
                <button onClick={signup} className="text-xl w-24 h-10 bg-[#85ffff] hover:bg-[#85ffa5] rounded-md mt-4">Submit</button>
            </div>
        </div>
        </div>
    </>
    );
};
