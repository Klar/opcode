# opcode
Counts the different start OPCode output's of Bitcoin SV's last 1000 Transactions.


## Output
Example Script output
```
{
    "OP_DUP": {
        "count": 573,
        "txExample": {
            "_id": "5d3ca0085c382d167cbd5a2a",
            "blk": {
                "i": 593032
            },
            "out": [
                {
                    "str": "OP_DUP OP_HASH160 31f2bece272b5d346aa56d09101dd7306d9a3075 OP_EQUALVERIFY OP_CHECKSIG"
                },
                {
                    "str": "OP_RETURN b9e11b6d5b11724c2c7445e4ce7ebe38d6ab9a60cf383f16f1e32a75d3628136147bbcb3"
                }
            ],
            "tx": {
                "h": "fff897ccc392e485480302927e99336d7ab2473e29cb61366423f5c6bd88d697"
            }
        }
    },
    "OP_HASH160": {
        "count": 6,
        "txExample": {
            "_id": "5d3ca0085c382d167cbd5a2d",
            "blk": {
                "i": 593032
            },
            "out": [
                {
                    "str": "OP_HASH160 ce52e8c4363d94f62593cd2cf5d6d131fd1a3b5f OP_EQUAL"
                },
                {
                    "str": "OP_HASH160 3146e25d37d215817edc100c7109179d072ccec3 OP_EQUAL"
                }
            ],
            "tx": {
                "h": "c9800cfc9b075a3bd4ffc2e9096c55d7fcfa7982645239716c3fc00ee74423ec"
            }
        }
    },
    "OP_RETURN": {
        "count": 549,
        "txExample": {
            "_id": "5d3ca0085c382d167cbd5a2a",
            "blk": {
                "i": 593032
            },
            "out": [
                {
                    "str": "OP_DUP OP_HASH160 31f2bece272b5d346aa56d09101dd7306d9a3075 OP_EQUALVERIFY OP_CHECKSIG"
                },
                {
                    "str": "OP_RETURN b9e11b6d5b11724c2c7445e4ce7ebe38d6ab9a60cf383f16f1e32a75d3628136147bbcb3"
                }
            ],
            "tx": {
                "h": "fff897ccc392e485480302927e99336d7ab2473e29cb61366423f5c6bd88d697"
            }
        }
    }
}
```
