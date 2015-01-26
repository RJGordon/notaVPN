import urllib2, os

CURVERSION = "1.0"

def checkVersion(url):
	response = urllib2.urlopen(url)
	versionNum = response.read()
	printVal = ""
	if versionNum == CURVERSION:
		printVal = "notaVPN is currently up-to-date."
	else:
		printVal = "notaVPN is outdated and must be updated immidiately."
	print("{} | Version Number: {}".format(printVal, CURVERSION)

	## DO UPDATE ## 


# bannana's code #
def getURL(url):
	buffer =  StringIO()

	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()

	return buffer.getvalue()

def findn(string, substring, n):
	parts = string.split(substring, n+1)
	if len(parts)<=n+1:
		return -1
	return len(string)-len(parts[-1])-len(substring)

def getPassword(vpn):
	string = getURL(vpns[vpn]['url'])
	index = findn(string, vpns[vpn]['str'], int(vpns[vpn]['nth']))
	return string[index+int(vpns[vpn]["sio"]):index+int(vpns[vpn]["eio"])]

