import json, win32ras, util

server_info = open("servers.json")
servers = json.load(server_info)

def dispServers():

	for x, i in enumerate(servers):
		print(x, i["dsp"])
		
def winConnect(server):
	name = servers[server]["dsp"]
	address = servers[server]["srv"]
	username = servers[server]["usr"]
	password = util.getPassword(server)

	hdl, retcode = win32ras.Dial (None, None, (name, address, "", username, password, ""), None)

winConnect(1)