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






