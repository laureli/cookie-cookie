seeAllTheCookies(function(cookieData){
    console.log('number of cookies',cookieData.length)
    var allCookieArray = [];
    for (i=0; i<cookieData.length; i++) {
        allCookieArray.push(cookieData[i]);
    }
    localStorage.allCookieArray = allCookieArray
    console.log('array of cookie info is:', allCookieArray)

    $.ajax({
        type: "POST",
        url: 'http://localhost:5000/read_cookies',
        contentType: 'application/json',
        data: JSON.stringify({
            cookies: allCookieArray,
            username: 'lkm'
        }),
        dataType: 'json', 
        success: function (response) {
            console.log(response);
            alert(response); 
        }
    })
});


getSpecificCookie("CookieName", function(cookieData){
    console.log("here is cookieData: ")
    console.log(cookieData)
});


removeCookie(function(removedCookieData) {
    console.log("here is the cookie that was removed: ")
    console.log(removedCookieData)
});





