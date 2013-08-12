
// // ##################################### GET ALL THE COOKIES into an array

// function seeAllTheCookies (callback){
//     console.log("getting all the cookies, simply.")
//     chrome.cookies.getAll({}, callback);
// }

// seeAllTheCookies(function(cookieData){
//     console.log('number of cookies',cookieData.length)
//     var allCookieArray = [];
//     for (i=0; i<cookieData.length; i++) {
//         allCookieArray.push(cookieData[i]);
//     }
//     localStorage.allCookieArray = allCookieArray
//     console.log('array of cookie info is:', allCookieArray)

//     $.ajax({
//         type: "POST",
//         url: 'http://localhost:5000/read_cookies',
//         contentType: 'application/json',
//         data: JSON.stringify({
//             cookies: allCookieArray,
//             username: 'lkm'
//         }),
//         dataType: 'json', 
//         success: function (response) {
//             console.log(response);
//             alert(response); 
//         }
//     })
// });

// ######################## set single cookie to the browser


// function setCookietoBrowser(url, name, value, domain) {
//     console.log("a cookie is going to get set to your browser - 2")
//     chrome.cookies.set({
//         'url':url,
//         'name':name,
//         'domain': domain,
//         'value': value
//     })
// }

// function sendCookie() {
//     $.ajax({
//         type: "GET",
//         url: 'http://localhost:5000/set_browser_cookie',
//         // contentType: 'application/json',
//         // dataType:'json',
//         success: function (response) {
//             var cookies = response.cookies;
//             console.log('cookies')
//             console.log(response, 'a cookie got set, yah');
//             console.log(response)

//             setCookietoBrowser(cookies[0]['url'],
//                             cookies[0]['name'],
//                             cookies[0]['value'],
//                             cookies[0]['domain']
//             )
//         }
//     })
// }



// // ######################## get() single cookie, the cookie is returned
                            // as an OBJECT, diff from getAll()

// function getSpecificCookie (cookieName, callback){
//     console.log("called getCookie")
//     chrome.cookies.get({
//         'url':'http://www.eventbrite.com',
//         'name':'mgrefby'
//     },
//     function(data){
//         callback(data);
//     });
// }

// getSpecificCookie("CookieName", function(cookieData){
//     console.log("here is cookieData: ")
//     console.log(cookieData)
// });


// // //######################## delete a single cookie

// function removeCookie(cookieName, callback) {
//     console.log("a cookie is getting removed from the browser")
//     chrome.cookies.remove({
//         'url':'http://www.mashable.com',
//         'name':'__utma'
//     },
//     function(data){
//         callback(data);
//     });
// }

// ("CookieName", function(removedCookieData) {
//     console.log("here is the cookie that was removed: ")
//     console.log(removedCookieData)
// });




// // // // ############################ get cookies from a specific URL - two funcs
// function getCookies(){
//     chrome.cookies.getAll({},function (cookies) {
//         console.log(cookies.length);
//         var interestingCookies = [];
//         for(i=0;i<cookies.length;i++) {
//             if (isInterestingCookie(cookies[i])) {
//                 console.log('cookie number',i);
//                 console.log(cookies[i]);
//                 interestingCookies.push(cookies[i]);
//             }
//         }   
//         localStorage.interestingCookies = interestingCookies;
//     });
// }
// window.onload=getCookies;

//     // the code below - both chunks - work with the above function to push 
//     // specified cookies to an array called interestingCookies

// function isInterestingCookie(cookie) {
//     console.log('get cookies with one shared parameter')
//     return cookie.domain == ".eventbrite.com";
// }

// function isInterestingCookie(cookie) {
//     console.log('get a cookie with two parameters')
//     return cookie.domain == ".eventbrite.com" && 
//     cookie.name == 'ebtv';
// }



// // #####################################  TEST SPACE
