
function seeAllTheCookies (callback){
    console.log("getting all the cookies, b/c i love you.")
    chrome.cookies.getAll({}, callback);
}

seeAllTheCookies(function(cookieData){
    console.log('number of cookies',cookieData.length)
    var allCookieArray = [];
    for (i=0; i<cookieData.length; i++) {
        allCookieArray.push(cookieData[i]);
    }
    localStorage.allCookieArray = allCookieArray
   
    var i=0; while (i<15) {i++
        $('#summary_table').append('<tr><td>'+i+'</td><td>'+allCookieArray[i]['domain']+'</td><td>'+allCookieArray[i]['name']+'</td><td>'+allCookieArray[i]['value']+'</td></tr>')
    }
});

