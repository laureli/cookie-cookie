
function seeAllTheCookies (callback){
    chrome.cookies.getAll({}, callback);
}
seeAllTheCookies(function(cookieData) {
    if (cookieData) {
        console.log('number of cookies in cookieData',cookieData.length)
        localStorage.cookieData = cookieData;
       var cookielooplength = cookieData.length<20?cookieData.length: 20;
        // for (i=0; i<cookieData.length; i++) {
        for (i=0; i<20; i++) {
            $('#summary_table').append('<tr><td>'+(i+1)+'</td><td>'+
            cookieData[i]['domain']+'</td><td>'+
            cookieData[i]['name']+'</td><td>'+
            cookieData[i]['value']+'</td></tr>')
        }
    }
});


// #################### display cookies on the extension ###########

function grabCookies(callback) {
    $.ajax({
        type: "POST",
        url: 'http://localhost:5000/show_cookies',
        success: function (response) {
            callback(response);
            console.log(response);
        },
        error: function (response) {
            alert(response);
            alert('the server is taking a time out. please call back later.');
        }
    })
}

function viewCookies(data) {
    console.log('number of cookies in data.dbCookies', data.dbCookies.length)

    // for (i=0; i<data.dbCookies.length; i++) {
    for (i=0; i<20; i++) {
        $('#swap_table').append('<tr class="cookierow"><td class="key">'+i+'</td><td>'+
            data.dbCookies[i]['domain']+'</td><td>'+
            data.dbCookies[i]['name']+'</td><td>'+
            data.dbCookies[i]['value']+'</td></tr>')
    }
    $('.cookierow').click(function() {
        $(this).toggleClass('cookierow_selected')
    });
    localStorage.dbCookiesArray = JSON.stringify(data.dbCookies);

}

// ###################### loaded cookies on button click from manager.html on extension  ####### 

function sendAlltheCookies(callback) {
    chrome.cookies.getAll({}, callback);
}

var cookieCallback = function (cookieData) {
    console.log('number of cookies',cookieData.length)
    var sendCookieArray = [];
    for (i=0; i<cookieData.length; i++) {
        sendCookieArray.push(cookieData[i]);
    }
    // localStorage.sendCookieArray = sendCookieArray;
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
        },
        error: function (response) {
            alert('the database error message fired. why? are you logged in?')
        }
    })
}


// ################# setting cookies for fun and... profit

function setSelectedCookiesFromLocal(cookiesToSet) {
    alert('setSelectedCookiesfromLocal is running');
    // alert('cookies to set are '+cookiesToSet);
    var dbCookies = JSON.parse(localStorage.getItem('dbCookiesArray'));

for (i=0; i<dbCookies.length; i++) {
    $.extend(dbCookies[i], {url:'http://'+dbCookies[i].domain})
}

    for (i=0; i<cookiesToSet.length; i++) {
        setSelectedCookie(dbCookies[cookiesToSet[i]])
    }
}

function setSelectedCookie(cookie) {
    alert('the cookies are supposed to get set.');
    console.log(cookie.url);
    chrome.cookies.set({
        'name':cookie.name,
        'value':cookie.value,
        'domain':cookie.domain,
        'url':cookie.url
    })
    alert('you got to the other end')
}









// function kyle() {}
// var kyle = function () {};
