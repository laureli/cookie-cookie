// GET COOKIES AND PUT THEM INTO ARRAY CALLED 'interestingCookies'

function getCookies(){
    chrome.cookies.getAll({},function (cookies) {
        console.log(cookies.length);
        var interestingCookies = [];
        for(i=0;i<cookies.length;i++) {
            if (isInterestingCookie(cookies[i])) {
                console.log('cookie number',i);
                console.log(cookies[i]);
                interestingCookies.push(cookies[i]);
            }
        }   
        localStorage.interestingCookies = interestingCookies;
    });
}

    // WORKS WITH THE FUNCTION BELOW:
    //     function isInterestingCookie(cookie) {
    //         console.log('get a cookie with two parameters')
    //         return cookie.domain == ".eventbrite.com" && 
    //         cookie.name == 'ebtv';
    //     }

// READ COOKIES AND OUTPUT INTO ARRAY, CONVERT TO JSON

function seeAllTheCookies (callback){
    console.log("getting all the cookies, simply.")
    chrome.cookies.getAll({}, callback);
}

// SET COOKIE TO BROWSER

function setCookietoBrowser(url, name, value, domain) {
    console.log("a cookie is going to get set to your browser - 2")
    chrome.cookies.set({
        'url':url,
        'name':name,
        'domain': domain,
        'value': value
    })
}

// SEND A COOKIE IN JSON - WORKS WITH setCookietoBrowser

function sendCookie() {
    $.ajax({
        type: "GET",
        url: 'http://localhost:5000/set_browser_cookie',
        // contentType: 'application/json',
        // dataType:'json',
        success: function (response) {
            var cookies = response.cookies;
            console.log('cookies')
            console.log(response, 'a cookie got set, yah');
            console.log(response)

            setCookietoBrowser(cookies[0]['url'],
                            cookies[0]['name'],
                            cookies[0]['value'],
                            cookies[0]['domain']
            )
        }
    })
}

// DELETE A SPECIFIC COOKIE -- SPECIFIED HERE

function removeCookie(cookieName, callback) {
    console.log("a cookie is getting removed from the browser")
    chrome.cookies.remove({
        'url':'http://www.mashable.com',
        'name':'__utma'
    },
    function(data){
        callback(data);
    });
}








