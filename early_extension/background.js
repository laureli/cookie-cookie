

//############################# GET ALL OF THE COOKIES
//############################# with JSON-esque formatting

function getAlltheCookies(){
     chrome.tabs.query({"status":"complete","windowId":chrome.windows.WINDOW_ID_CURRENT,
        "active":true}, 
        function(tab){
            console.log(JSON.stringify(tab));
            chrome.cookies.getAll({"url":tab[0].url},function (cookie){
                console.log(cookie.length);
                allCookieData = "";
    // next line gets all the cookies.  i turned it off.  am getting 15
                for(i=0;i<cookie.length;i++){
                   // for(i=0;i<15;i++){ 
                    console.log("cookie is #"+i)
                    console.log(JSON.stringify(cookie[i]));

                    allCookieData = allCookieData + JSON.stringify(cookie[i]);
                }
                localStorage.currentgetAlltheCookies = allCookieData;
            });
        });
    }
window.onload=getAlltheCookies;

//############################# GET SPECIFIED COOKIES
//############################# USING localStorage w/o JSON


function getCookie(){
    chrome.cookies.getAll({},function (cookies){
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
window.onload=getCookie;

function isInterestingCookie(cookie) {
    return cookie.domain == ".mashable.com";
}







