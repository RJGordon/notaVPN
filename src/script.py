#!/usr/bin/python

import sys
import pycurl
from StringIO import StringIO

vpns = {
	"vpnbook": {
		"url": "http://www.vpnbook.com",
		"sio": 10,
		"eio": 18,
		"str": "Password:",
		"nth": 0
	},
	"vpnmask": {
		"url": "http://vpnmask.com",
		"sio": 10,
		"eio": 18,
		"str": "Password:",
		"nth": 3
	},
	"vpnmeDE": {
		"url": "https://www.vpnme.me/freevpn.html",
		"sio": 34,
		"eio": 40,
		"str": "Password",
		"nth": 0
	},
	"vpnmeUS": {
		"url": "https://www.vpnme.me/freevpn.html",
		"sio": 56,
		"eio": 62,
		"str": "Password:",
		"nth": 0

	},
	"vpnmeUS2": {
		"url": "https://www.vpnme.me/freevpn.html",
		"sio": 78,
		"eio": 84,
		"str": "Password:",
		"nth": 0
	}
}

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

if __name__ == "__main__":
	print(getPassword("vpnbook"))
	print(getPassword("vpnmask"))
	print(getPassword("vpnmeDE"))
	print(getPassword("vpnmeUS"))
	print(getPassword("vpnmeUS2"))
