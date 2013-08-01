function sendRequest() {
	url= 'monster.py';
	request.open('GET', url, true);
	request.onreadystatechange = processRequest;
	requst.send(null);
}