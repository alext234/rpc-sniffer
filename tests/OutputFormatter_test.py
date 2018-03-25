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
		

	def test_OutputFormatterMethodCall(self):
		jsonObject = json.loads(\
			'{"id": 1, "params": [], "method": "web3_clientVersion", "jsonrpc": "2.0"}')
		formattedOutput = self.outputFormatter(jsonObject)
		expectedOutput = str(jsonObject['id']).ljust(Config.ID_SIZE) + \
			jsonObject['method'].ljust(Config.METHOD_SIZE) + \
			str(jsonObject['params']).ljust(Config.PARAMS_SIZE)
					
		self.assertEqual(formattedOutput, expectedOutput)
		

	def test_OutputFormatterResponse(self):
		jsonObject = json.loads(\
		'{"jsonrpc":"2.0","id":1,"result":"Geth/v1.8.2-stable/linux-amd64/go1.9.2"}')
		formattedOutput = self.outputFormatter(jsonObject)
		expectedOutput = str(jsonObject['id']).ljust(Config.ID_SIZE) + \
			' '.ljust(Config.METHOD_SIZE) + \
			' '.ljust(Config.PARAMS_SIZE) + \
			jsonObject['result'].ljust(Config.RESULT_SIZE)
			
					
		self.assertEqual(formattedOutput, expectedOutput)
		
		
		
		