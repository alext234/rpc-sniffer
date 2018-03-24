import unittest
import os 
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
		Test that PacketDecoder should be able to parse HTTP packets
		"""
		packets = rdpcap(self.dataDir + '/web3_clientVersion.pcap')

		for packet in packets:
			self.packetDecoder (packet)