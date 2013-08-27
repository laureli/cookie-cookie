CookieHuntr is a tool that allows Chrome users to swap white-listed cookies across a network of users.  

The cookie swap enables people to browse more anonymously and to experience the internet from someone else's perspective. This project uses a combination of web UI, for user management and synchronizing browser states, as well as a Chrome browser extension.  Chrome extensions have a increased access rights to create, modify, and delete data native to the browser.  

CookieHuntr leverages this to export a user's cookies from the Chrome cookiejar using JSON and AJAX to store whitelisted cookies in the PostrgreSQL database.  The user can query the database to select new cookies to install on their browser.  The selected cookies are initially stored in LocalStorage on the browser, which allows the user to select cookies to be installed with a high level of granularity.  Once selected, the cookies are copied into the browser cookiejar.  This two step process sidesteps restrictions on cross-origin permissions.  The cookies are inserted into the user's computer as if natively installed.   

Security and privacy concerns are initially being managed through the use of a limited whitelist based on domain name and cookie name.  Additional security and information management features are under development.

CookieHuntr uses Python, JavaScript, jQuery, AJAX, JSON, PostreSQL, Flask, WTForms, Flask-Login, Jinja, HTML & Chrome browser APIs.
