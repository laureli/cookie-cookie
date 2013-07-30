// // ############################ get cookies from a specific URL - two funcs
// function getCookie(){
//     chrome.cookies.getAll({},function (cookies){
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
// window.onload=getCookie;


// function isInterestingCookie(cookie) {
//     return cookie.domain == ".here_is_the_URL.com";
// // }

//######################## get single cookie

function getSpecificCookie (cookieName, callback){
    console.log("called getCookie")
    chrome.cookies.get({
        'url':'http://www.here_is_the_URL.com',
        'name':'damn_this_is_a_cookie'
    },
    function(data){
        callback(data);
    });
}

getSpecificCookie("CookieName", function(cookieData){
    console.log("here is cookieData: ")
    console.log(cookieData)
});


// //######################## delete a single cookie

// function deleteCookie(cookieName, callback) {
//     console.log("a cookie is getting removed from the browser")
//     chrome.cookies.remove({
//         'url':'http://www.mashable.com',
//         'name':'__utma'
//     },
//     function(data){
//         callback(data);
//     });
// }

// deleteCookie("CookieName", function(removedCookieData) {
//     console.log("here is the cookis that was removed: ")
//     console.log(removedCookieData)
// });

//######################## set single cookie to the browser


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

