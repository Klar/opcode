#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import base64
import json
import requests


epochtimeNow = time.time()
epochtimeHourBack = epochtimeNow - 3600

epochtimeNow = str(epochtimeNow)
epochtimeHourBack = str(epochtimeHourBack)

bitdbString = '{"v":3,"e":{"out.b1":"hex"},"db":["c"],"q":{"aggregate":[{"$match":{"$and":[{"blk.t":{"$gte":' + epochtimeHourBack + ',"$lte":'+ epochtimeNow + '}}]}}],"find":{},"project":{"tx.h":1,"out.str":1}}}'

bitdbString64 = base64.b64encode(bitdbString.encode()).decode("utf-8")
print(bitdbString64)

url = "https://bitgraph.network/q/" + bitdbString64
api_token = ''
headers = {'key': api_token}

response = requests.get(url, headers=headers)
response = response.json()
confirmedResponse = response['c']

print(confirmedResponse)

opoutput = dict()
opreturn = dict()

opoutput["OP_DUP"] = 0
opoutput["OP_HASH160"] = 0

for tx in confirmedResponse:
    print(tx)
    txID = tx["tx"]["h"]
    for data in tx["out"]:
        data = data["str"].split(" ")
        if data[0] == "OP_DUP":
            opoutput["OP_DUP"] = opoutput["OP_DUP"] + 1
        elif data[0] == "OP_RETURN":
            # opreturndict = dict()
            print(data)
            # print(len(data))
            if len(data) == 2:
                ascii = data[1].decode("hex").encode("utf-8")
                print(ascii)
            elif len(data) == 3:
                prefix = data[1]
                print(prefix)
                if len(data[2]) == 64:
                    txID = data[2]
                    print(txID)
                else:
                    ascii = data[2].decode("hex").encode("utf-8")
                    print(ascii)
            elif len(data) == 4:
                prefix = data[1]
                txID = data[2]
                if len(data[3]) > 1:
                    ascii = data[3].decode("hex").encode("utf-8")
                    print(ascii)
                print(prefix)
                print(txID)
            print("\n\n")
            # opreturndict["txID"] = txID
            # opreturn["prefix"] =
            # opreturn["txID"] = txID
            # opreturn[txID] = opreturndict
        elif data[0] == "OP_HASH160":
            opoutput["OP_HASH160"] = opoutput["OP_HASH160"] + 1
        else:
            opoutput[data[0]] = 0

prefixes = dict()

# print(opreturn)

# print(len(prefixes))
opoutput["OP_RETURN"] = prefixes

print(json.dumps(opoutput, indent=4, sort_keys=True))
