
function seeAllTheCookies (callback){
    console.log("getting all the cookies, b/c i love you.")
    chrome.cookies.getAll({}, callback);
}

seeAllTheCookies(function(cookieData) {
    console.log('number of cookies',cookieData.length)
    var allCookieArray = [];
    for (i=0; i<cookieData.length; i++) {
        allCookieArray.push(cookieData[i]);
    }
    localStorage.allCookieArray = allCookieArray;
   
    for (i=0; i<allCookieArray.length; i++) {
            $('#summary_table').append('<tr><td>'+i+'</td><td>'+
            allCookieArray[i]['domain']+'</td><td>'+
            allCookieArray[i]['name']+'</td><td>'+
            allCookieArray[i]['value']+'</td></tr>')
    }
});


// modify this function to send cookies to the database without server interaction.
// actually, i can send these to the database through the server.  i need to 
// figure out how to send content from extension to server.


// ################################## all the cookies are getting loaded 
// from the button on manager.html.

function sendAlltheCookies(callback) {
    chrome.cookies.getAll({}, callback);
    console.log("mandar galletas por que me ama.");
}

var cookieCallback = function (cookieData) {
    console.log('number of cookies',cookieData.length)
    var sendCookieArray = [];
    for (i=0; i<cookieData.length; i++) {
        sendCookieArray.push(cookieData[i]);
    }
    localStorage.sendCookieArray = sendCookieArray;
    console.log('array of cookie info is:', sendCookieArray)

    $.ajax({
        type: "POST",
        url: 'http://localhost:5000/load_cookies',
        contentType: 'application/json',
        data: JSON.stringify({
            cookies: sendCookieArray,
            username: 'test'
        }),
        dataType: 'json', 
        success: function (response) {
            console.log(response);
            // alert(response); 
        }
    })
}

function kyle() {}

var kyle = function () {};

sendAlltheCookies(cookieCallback);

console.log('send cookies to database');
        $("#send_btn").click(function() {
            console.log('send cookies to database');
            sendAlltheCookies(cookieCallback);
        });


