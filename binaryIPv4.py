# Pulls BinaryEdge's scanners' IPv4 addresses located here: https://api.binaryedge.io/v1/minions
# BinaryEdge  scans the internet and acquire data that can be used in threat intelligence feeds or security reports.
# Documentation https://docs.binaryedge.io/

import requests

file = open("binaryEdgeBlockList.txt", "w")

# BinaryEdge's scanners' IPv4 addresses
url="https://api.binaryedge.io/v1/minions"

# Verify=False this prevents the SSL check and throwing errors related to it
request = requests.get(url, verify=False) 

ipList = request.json()["scanners"]
ipCount = 0


for ip in ipList:
    ipCount+=1
    #print(ip)
    file.write(f"{ip}\n")

file.close()

print(f"Total IPv4 count: {ipCount}")

#print(request.json()["scanners"])