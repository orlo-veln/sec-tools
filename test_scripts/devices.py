devices = [
	{"ip": "192.168.68.1", "type": "router", "suspicious": False},
	{"ip": "192.168.68.57", "type": "chromecast", "suspicious": False},
	{"ip": "192.168.68.60", "type": "cat feeder", "suspicious": True},
]

for device in devices:
	if device["suspicious"]:
		print(f"SUSPICIOUS: {device['ip']} - {device['type']}")
	else:
		print(f"OK: {device['ip']} - {device['type']}")

