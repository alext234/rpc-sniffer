#!/usr/bin/env python

import logging
# hide some warning message from scaopy at startup
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from rpcsniffer import *
from rpcsniffer.PacketDecoder import *
from rpcsniffer.OutputFormatter import *
logging.getLogger().setLevel(logging.INFO)


packetDecoder = PacketDecoder()
outputFormatter = OutputFormatter()

def sniffCallback(packet):
	jsonObject = packetDecoder(packet)
	if jsonObject is not None:
		print(outputFormatter(jsonObject))


loCounter=0
def sniffCallbackLo(packet):
	"""
	special handling for loopback interface, which will capture a packet twice
	"""
	global loCounter
	loCounter += 1
	if (loCounter % 2):
		sniffCallback(packet)
	
	
def main():
	logging.info("Sniff network packets and decode JSONRPC on HTTP")
	if len(sys.argv) < 2:
		print("Please input a .pcap file or a network interface to capture")
		exit(1)

	ifn = sys.argv[1]
	print(outputFormatter.columnTitles())
	if ifn.endswith(".pcap") or ifn.endswith(".cap"):
		sniff(offline=ifn, filter="tcp", prn=sniffCallback, store=False)
	else:
		# assuming it is a network interface
		prn = sniffCallback
		if ifn=='lo':
			prn = sniffCallbackLo 
		sniff(iface=ifn, filter="tcp", prn=prn, store=False)
		

if __name__ == '__main__':
	main()