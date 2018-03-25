import unittest
from rpcsniffer.OutputFormatter import *
from rpcsniffer import Config
import json

class PackerDecoderTestCase(unittest.TestCase):
	def setUp(self):
		self.outputFormatter = OutputFormatter()

	def tearDown(self):
		pass
	

	def test_OutputFormatterTitles(self):
		columnTitles = self.outputFormatter.columnTitles()
		expectedColumnTitles="id".ljust(Config.ID_SIZE) +\
			"method".ljust(Config.METHOD_SIZE) + \
			"params".ljust(Config.PARAMS_SIZE) + \
			"result".ljust(Config.RESULT_SIZE) 
		self.assertEqual(columnTitles, expectedColumnTitles)
		

	def test_OutputFormatterJsonObject(self):
		jsonObject = json.loads(\
			'{"id": 1, "params": [], "method": "web3_clientVersion", "jsonrpc": "2.0"}');
		formattedOutput = self.outputFormatter(jsonObject)
		expectedOutput = "" # TODO to set an expected output here
		
		self.assertEqual(formattedOutput, expectedOutput)