# Pulls BinaryEdge's scanners' IPv4 addresses located here: https://api.binaryedge.io/v1/minions
# BinaryEdge  scans the internet and acquire data that can be used in threat intelligence feeds or security reports.
# Documentation https://docs.binaryedge.io/
# Make it easy to block all BinaryEdge scanners' IPv4 addresses by throwing them in a plain-text file, with each address on a separate line.

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
    file.write(f"{ip}\n")

file.close()

print(f"Total IPv4 count: {ipCount}")
print("File creation complete.")
