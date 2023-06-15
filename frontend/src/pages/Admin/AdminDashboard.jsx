import { useEffect } from 'react';
import { validateCookie } from '../../helpers/validation';
import { CreateFlight } from './CreateFlight';
import { AddFlightTiming } from './AddFlightTiming';
import { DeleteFlight } from './DeleteFlight';
import { Toast } from '../../components/Login/toast';
import { GetFlights } from '../Flight/GetFlights';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import { getCookie } from '../../helpers/validation';


export const AdminDashboard = () => {

    const logoutAdmin = async () => {
        let cookie = getCookie(document.cookie);
        await fetch("/admin/logout", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "id": cookie
            },
        }).then((res) => {
            if ( res.status === 200 ) {
                document.cookie = "id   =; expires=Thu, 01 Jan 1970 00:00:00 UTC;";
                window.open("/admin/login", "_self");
            } else {
                alert("Failed to logout");
            }
        }) 
    }

    useEffect(() => {
        (async () => {
            if ( !(await validateCookie(document.cookie, "admin")) ) {
                window.open("/admin/login", "_self");
           }
        })();
    }, [])

    const createToast = () => {
        
    }

    return ( 
    <>
    <div>
        <div className='flex justify-end pr-10'>
            <FontAwesomeIcon onClick={logoutAdmin} className="ml-2 mt-9 hover:cursor-pointer" icon={faUser} title=""/>
        </div>
        <CreateFlight/>
        <AddFlightTiming/>
        <DeleteFlight/>
        <GetFlights/>
        <div>
            <p>Test Toast</p>
            <button onClick={createToast}>Test Toast</button>
        </div>
    </div>
    </>
    );
}