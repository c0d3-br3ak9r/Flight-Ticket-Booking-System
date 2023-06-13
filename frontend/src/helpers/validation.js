export const getCookie = (cookie) => {
    if ( cookie ) {
        cookie = cookie.split(";")[0];
        console.log(cookie);
        console.log(typeof cookie);
        if ( cookie.indexOf("=") ) {
            return cookie.split("=")[1];
        }
    }
    return "";
}

export const validateCookie = async (cki, usr) => {
    let url = "/authenticate";
    const cookie = getCookie(cki);
    if ( cookie === "" ) return false;
    let isSuccess;
    await fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "id": cookie
        },
        body: JSON.stringify({
            user : usr,
        }),
    }).then((res) => {
        if ( res.status === 200 ) {
            isSuccess = true;
        } else {
            isSuccess = false;
        }
    });
    return isSuccess;
}