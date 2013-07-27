function getCookie (cookieName, callback){
    console.log("called getCookie")
    chrome.cookies.get({
        'url':"http://www.strava.com",
        'name':"__utmc"
    },
    function(data){
        callback(data);
    });
}


getCookie("CookieName", function(cookieData){
console.log("here is cookieData: "+ cookieData)});

