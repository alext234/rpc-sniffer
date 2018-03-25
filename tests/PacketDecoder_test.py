import unittest
import os 
import logging
# hide some warning message from scaopy at startup
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *
from rpcsniffer.PacketDecoder import *

class PackerDecoderTestCase(unittest.TestCase):
	def setUp(self):
		self.testsDir = os.path.dirname(os.path.realpath(__file__))
		self.dataDir = self.testsDir + "/data"
		self.packetDecoder = PacketDecoder()

	def tearDown(self):
		pass
	

	def test_HttpPackets(self):
		"""
		PacketDecoder should be able to parse HTTP packets
		"""
		packets = rdpcap(self.dataDir + '/web3_clientVersion.pcap')

		numDecodedHttpPackets = 0
		for packet in packets:
			if self.packetDecoder(packet) is not None:
				numDecodedHttpPackets +=1
		
		self.assertEqual(numDecodedHttpPackets, 2)
			
	
	def test_methodCallRequest(self):
		"""
		PacketDecoder should decode correctly the json fields of a method call request
		"""
		packets = rdpcap(self.dataDir + '/web3_clientVersion_method_call.pcap')
		packet = packets[0] # there is only 1 packet in the file
		data = self.packetDecoder(packet)
		
		self.assertNotEqual(data, None)
		self.assertEqual(data['method'], "web3_clientVersion")
		self.assertEqual(data['params'], [])

	def test_methodCallResults(self):
		"""
		PacketDecoder should decode correctly the json fields of a method call response
		"""
		packets = rdpcap(self.dataDir + '/web3_clientVersion_result.pcap')
		packet = packets[0] # there is only 1 packet in the file
		data = self.packetDecoder(packet)
		
		self.assertNotEqual(data, None)
		self.assertNotEqual(data['result'], "")
		