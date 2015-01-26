import os, json

def getURL(url):
	buffer =  StringIO()

	c = pycurl.Curl()
	c.setopt(c.URL, url)
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()

	return buffer.getvalue()

def checkUpdates(curVers, url):
	retVal = False
	latestVersion = getURL(url)
	printVal = ""
	if versionNum == curVers:
		printVal = "notaVPN is currently up-to-date."
	else:
		printVal = "notaVPN is outdated and must be updated immidiately."
		retVal = True

	print("{} | Version Number: {}".format(printVal, curVers)
	return(retVal)

def findn(string, substring, n):
	parts = string.split(substring, n+1)
	if len(parts)<=n+1:
		return -1
	return len(string)-len(parts[-1])-len(substring)

def getPassword(vpn):
	server_data=open('servers.json')
	vpns = json.load(server_data)
	string = getURL(vpns[vpn]['url'])
	index = findn(string, vpns[vpn]['str'], int(vpns[vpn]['nth']))
	return string[index+int(vpns[vpn]["sio"]):index+int(vpns[vpn]["eio"])]
	
