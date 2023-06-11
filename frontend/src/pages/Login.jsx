import { useRef } from "react";

export const Login = () => {
    const usernameRef = useRef();
    const passwordRef = useRef();

    const login = () => {
        alert(usernameRef.current.value + passwordRef.current.value);
    };

    return (
    <>
        <div className="flex justify-center items-center flex-col m-auto h-screen bg-[#05ad32] border">
            <p className="text-3xl font-bold">Login</p>
            <div className="w-1/2 flex flex-row justify-evenly mt-8">
                <p className="text-xl">Username</p>
                <input ref={usernameRef} type="text" className="w-60 h-10 border-4 rounded-md focus:outline-none focus:ring focus:border-green-500" />
            </div>
            <div className="w-1/2 flex flex-row justify-evenly mt-8">
                <p className="text-xl">Password</p>
                <input ref={passwordRef} type="text" className="w-60 h-10 border-4 rounded-md focus:outline-none focus:ring focus:border-green-500" />
            </div>
            <button onClick={login} className="w-20 h-8 bg-[#85ffa5] rounded-md mt-8">Submit</button>
        </div>
    </>
    );
};
