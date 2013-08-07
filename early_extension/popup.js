
// function cookieinfo(){
//     chrome.cookies.getAll({},function (cookie){
//         console.log(cookie.length);
//         allCookieInfo = "";
//         for(i=0;i<cookie.length;i++){
//             console.log(JSON.stringify(cookie[i]));

//             allCookieInfo = allCookieInfo + JSON.stringify(cookie[i]);
//         }
//         localStorage.allCookieInfo = allCookieInfo;
//     });
// }
// window.onload=cookieinfo;




function seeAllTheCookies (callback){
    console.log("getting all the cookies, simply.")
    chrome.cookies.getAll({}, callback);
}

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

window.onload=cookieinfo;
