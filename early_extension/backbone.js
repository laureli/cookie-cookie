// ##################################### GET ALL THE COOKIES into an array

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
    console.log('array of cookie info is:', allCookieArray, 'now that is done.')
    // do an ajax post request to localhost:5000/whatever
});


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
//     console.log("here is the cookis that was removed: ")
//     console.log(removedCookieData)
// });

// ######################## set single cookie to the browser


// function setCookietoBrowser(cookieName, callback) {
//     console.log("a cookie is going to get set to your browser")
//     chrome.cookies.set({
// //the URL might need specific permissions?
//         'url':'http://www.here_is_the_URL.com',
//         'name':'damn_this_is_a_cookie',
//         'value':'laureli_made_this_cookie'
//     });
// }

// setCookietoBrowser('cookieName', function(cookieSetOnBrowser) {
//     console.log('this cookie was set -')
//     console.log(cookieSetOnBrowser)
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
