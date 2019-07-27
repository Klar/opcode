#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import base64
import json
import requests

api_token = '147GjmCAREtYv7FdfDivthzcmQLmdEhSYe'

def bitd(querry):

    bitdbString64 = base64.b64encode(querry.encode()).decode("utf-8")
    # print(bitdbString64)

    url = "https://genesis.bitdb.network/q/1FnauZ9aUH2Bex6JzdcV4eNX7oLSSEbxtN/" + bitdbString64
    headers = {'key': api_token}

    response = requests.get(url, headers=headers)
    response = response.json()
    confirmedResponse = response['c']

    return(confirmedResponse)

def getOutput(getOpTxs):
    opoutput = dict()
    opreturn = dict()

    OP_DUP = dict()
    OP_DUP["count"] = 0

    OP_HASH160 = dict()
    OP_HASH160["count"] = 0

    OP_RETURN = dict()
    OP_RETURN["count"] = 0

    for tx in getOpTxs:
        txID = tx["tx"]["h"]
        for data in tx["out"]:
            data = data["str"].split(" ")
            if data[0] == "OP_DUP":
                OP_DUP["count"] = OP_DUP["count"] + 1
                OP_DUP["txExample"] = tx
            elif data[0] == "OP_HASH160":
                OP_HASH160["count"] = OP_HASH160["count"] + 1
                OP_HASH160["txExample"] = tx
            elif data[0] == "OP_RETURN":
                OP_RETURN["count"] = OP_RETURN["count"] + 1
                OP_RETURN["txExample"] = tx
            else:
                opoutput[data[0]] = 0
            
            opoutput["OP_DUP"] = OP_DUP
            opoutput["OP_HASH160"] = OP_HASH160
            opoutput["OP_RETURN"] = OP_RETURN

    print(json.dumps(opoutput, indent=4, sort_keys=True))

getLatestBlockQuerry = '{"v":3,"q":{"db":["c"],"find":{},"limit":1},"r":{"f":"[.[] | .blk | { current_blockheight: .i} ]"}}'
getLatestBlock = bitd(getLatestBlockQuerry)
current_blockheight = getLatestBlock[0]["current_blockheight"]

getOpTxs = '{"e":{"out.b1":"hex"},"q":{"find":{"blk.i":'+ str(current_blockheight) +'},"limit":1000,"project":{"blk.i":1,"out.str":1,"tx.h":1}},"v":3}'

getOpTxs = bitd(getOpTxs)

getOutput(getOpTxs)
