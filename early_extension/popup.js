
console.log('send cookies to database');
$("#send_btn").click(function() {
   console.log('send cookies to database');
   sendAlltheCookies(cookieCallback);
});

console.log('getting cookies from DB and displaying in app');
$("#swap_btn").click(function() {
  alert('grab cookies from database');
  grabCookies(viewCookies);
});

$('.cookierow').click(function() {
  $(this).attr('id')
})