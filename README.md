[![Build Status](https://travis-ci.org/alext234/rpc-sniffer.svg?branch=master)](https://travis-ci.org/alext234/rpc-sniffer)

# rpc-sniffer
This tool captures network traffic and decode them if they contain (Ethereum) JSON RPC.
This might be useful in the following scenarios:

- You want to know the exact RPC requests and responses sent to and from your Ethereum node.
- You want to debug and understand what `web3` sends out.
- You want to capture the contents `web3` sends out in order to use them in a different program.
 

# Installation

The following assumes you already have Python virtualenv activated. 
If not you may need to add `sudo`  in front of the setup.py command.

- Via the `setup.py` script

```
(activate python virtualenv)
git clone https://github.com/alext234/rpc-sniffer
cd rpc-sniffer
python setup.py install
```

# Usage

A `pcap` file can be given as the parameter:

```
> rpc-sniffer.py  tests/data/web3_clientVersion.pcap 
INFO:root:Sniff network packets and decode JSONRPC on HTTP
id        method                        params                                  result                                  
1         web3_clientVersion            []                                      
1                                                                               Geth/v1.8.2-stable/linux-amd64/go1.9.2  

```

Or a network interface can be given, for example with the local loopback interface `lo` (superuser is needed):

```
> sudo su

> (activate python virtualenv)

> rpc-sniffer.py lo

```
You will able to see the decoded traffic when you interact with a local RPC node via web3, for example.

```
id        method                        params                                  result                                  
1         eth_accounts                  []                                      
1         eth_getTransactionCount       ['0x70974f6673fa922eac3c2cd433d762e93db9399e', 'latest']
1                                                                               0x30                                    
1         net_version                   []                                      
1                                                                               99                                      
1         eth_gasPrice                  []                                      
1                                                                               0x430e23400                             
```


# Limitations

- This tool does not support encrypted SSL traffic (e.g. when you interact with an infura.io node).

- This tool does not support RPC traffic that spans multiple packets (development is in progress for this feature).