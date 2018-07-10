import urllib.request
try:
	url = "https://www.google.com/search?q=test"
	hdrs = 	{}
	hdrs["User-Agent"] = "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
	req = urllib.request.Request(url, headers=hdrs)
	resp = urllib.request.urlopen(req)
	respData = resp.read()
	file = open("headers.txt","w")
	file.write(str(respData))
	file.close()
except Exception as e:
	print(e)
