//############################# GET ALL OF THE COOKIES
    //############################# with JSON-esque formatting

// function getAlltheCookies(){
//      chrome.tabs.query({"status":"complete","windowId":chrome.windows.WINDOW_ID_CURRENT,
//         "active":true}, 
//         function(tab){
//             console.log(JSON.stringify(tab));
//             chrome.cookies.getAll({"url":tab[0].url},function (cookie){
//                 console.log(cookie.length);
//                 allCookieData = "";
//     // next line gets all the cookies.  i turned it off.  am getting 15
//                 // for(i=0;i<cookie.length;i++){
//                 for(i=0;i<50;i++){ 
//                     console.log("cookie is #"+i)
//                     console.log(JSON.stringify(cookie[i]));

//                     allCookieData = allCookieData + JSON.stringify(cookie[i]);
//                 }
//                 localStorage.currentgetAlltheCookies = allCookieData;
//             });
//         });
//     }
// window.onload=getAlltheCookies;


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


// // // ############################ get cookies from a specific URL - two funcs
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
window.onload=getCookies;

    // this works with the above function to push 
    //specified cookies to an array called interestingCookies

// function isInterestingCookie(cookie) {
//     console.log('get cookies with one shared parameter')
//     return cookie.domain == ".eventbrite.com";
// }

function isInterestingCookie(cookie) {
    console.log('get a cookie with two parameters')
    return cookie.domain == ".eventbrite.com" && 
    cookie.name == 'ebtv';
} 












