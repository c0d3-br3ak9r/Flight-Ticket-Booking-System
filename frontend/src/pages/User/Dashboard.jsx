import { useEffect } from 'react';
import { validateCookie } from '../../helpers/validation';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import { getCookie } from '../../helpers/validation';
import { GetFlights } from '../Flight/GetFlights';

export const Dashboard = () => {

    const logoutAdmin = async () => {
        let cookie = getCookie(document.cookie);
        await fetch("/logout", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "id": cookie
            },
        }).then((res) => {
            if ( res.status === 200 ) {
                document.cookie = "id   =; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
                window.open("/login", "_self");
            } else {
                alert("Failed to logout");
            }
        }) 
    }

    useEffect(() => {
        (async () => {
            if ( !(await validateCookie(document.cookie, "user")) ) {
                window.open("/login", "_self");
           }
        })();
    }, [])

    return (
    <>
    <div>
        <div className='flex justify-end pr-10'>
            <FontAwesomeIcon onClick={logoutAdmin} className="ml-2 mt-9 hover:cursor-pointer" icon={faUser} title=""/>
        </div>
        <GetFlights/>
    </div>
    </>
    );
};