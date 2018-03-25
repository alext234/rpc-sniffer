[![Build Status](https://travis-ci.org/alext234/rpc-sniffer.svg?branch=master)](https://travis-ci.org/alext234/rpc-sniffer)

# rpc-sniffer
This tool captures network traffic and decode them if they contain (Ethereum) JSON RPC.
This might be useful in the following scenarios:

- You want to know the exact RPC requests and responses sent to and from your Ethereum node.
- You want to debug and understand what `web3` sends out.
- You want to capture the contents `web3` sends out in order to use them in a different program.
 

# Installation

The following assumes you already have Python virtualenv activated. 
If not you may need to add `sudo`  in front of the setup.py command and the pip command.

- Via the `setup.py` script

```
git clone https://github.com/alext234/rpc-sniffer
cd rpc-sniffer
python setup.py install
```

- Or  via `pip`


```
pip install rpcsniffer
```

# Usage
TODO


# Limitations

- This tool does not support encrypted SSL traffic (e.g. when you interact with an infura.io node).

- This tool does not support RPC traffic that spans multiple packets (development is in progress for this feature).