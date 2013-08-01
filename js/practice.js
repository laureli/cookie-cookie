function sendRequest() {
	url= 'monster.py';
	request.open('GET', url, true);
	request.onreadystatechange = processRequest;
	requst.send(null);
}

function processRequest() {
	if (request.readyState == 4) {
		if (request.status == 200) {
			processResponse(request);
		} else {
			alert('error loading page '+
				request.status + ':' +
				request.statusText);
		}
	}
}