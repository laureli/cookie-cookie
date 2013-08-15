
function seeAllTheCookies (callback){
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


// #################### display cookies on the extension ###########

// grabCookies(viewCookies);

function grabCookies(callback) {
    $.ajax({
        type: "POST",
        url: 'http://localhost:5000/show_cookies',
        contentType: 'application/json',
        dataType: 'json', 
        success: function (response) {
            callback(response);
            console.log(response);
        }
    })
}

function viewCookies(data) {
    console.log('number of cookies', data.dbCookies.length)

    // for (i=0; i<data.dbCookies.length; i++) {
    for (i=0; i<20; i++) {
        $('#swap_table').append('<tr><td>'+i+'</td><td>'+
            data.dbCookies[i]['domain']+'</td><td>'+
            data.dbCookies[i]['name']+'</td><td>'+
            data.dbCookies[i]['value']+'</td></tr>')
    }
}

// ###################### loaded cookies on button click from manager.html on extension  ####### 

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

sendAlltheCookies(cookieCallback);
// console.log('send cookies to database');
//         $("#send_btn").click(function() {
//             console.log('send cookies to database');
//             sendAlltheCookies(cookieCallback);
//         });




















// function kyle() {}
// var kyle = function () {};
