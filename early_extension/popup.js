var pickedCookies=['if','this','then','that']

// send cookies to the database
$("#send_btn").click(function() {
   console.log('send cookies to database');
   sendAlltheCookies(cookieCallback);
   alert('thanks for sending cookies to the database')
});


// loads cookies from DB and populates table
$("#swap_btn").click(function() {
  grabCookies(viewCookies);
});

// // button click installs cookies on browser
$("#get_btn").click(function() {
	$("#swap_table tr.cookierow_selected td.key").each(
		function() { 
		console.log(this.textContent);
	})
});  
