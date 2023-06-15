export const getCookie = (cookie) => {
    console.log(cookie);
    if ( cookie.indexOf("=")  !== -1 ) {
        return cookie.split("=")[1];
    }
    return "";
}

export const validateCookie = async (cki, usr) => {
    let url = "/authenticate";
    const cookie = getCookie(cki);
    console.log(cookie);
    if ( !cookie ) return false;
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

