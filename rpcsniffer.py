#!/usr/bin/env python

import logging
# hide some warning message from scaopy at startup
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from rpcsniffer import *
logging.getLogger().setLevel(logging.INFO)

def main():
	logging.info("Sniffer network packets and decode JSONRPC on HTTP")

if __name__ == '__main__':
	main()