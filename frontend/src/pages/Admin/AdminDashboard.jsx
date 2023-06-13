import { useEffect } from 'react';
import { getCookie, validateCookie } from '../../helpers/validation';
import { CreateFlight } from './CreateFlight';
import { AddFlightTiming } from './AddFlightTiming';
import { DeleteFlight } from './DeleteFlight';

export const AdminDashboard = () => {

    useEffect(() => {
        if ( ! validateCookie(document.cookie, "admin") ) {
            window.open("/admin/login", "_self");
        }
    }, [])

    return ( 
    <>
    <div>
        <CreateFlight/>
        <AddFlightTiming/>
        <DeleteFlight/>
    </div>
    </>
    );
}