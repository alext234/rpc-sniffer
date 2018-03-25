from scapy.all import *
import json
import logging

class PacketDecoder:
	def __init__(self):
		pass
	
	
	def isHttp(self, packet):
		"""
		returns (isHttp, httpPayload)
		"""
		defaultReturn = (False, None)
		
		if not packet.haslayer(TCP):
			return defaultReturn 
		try:
			payload = bytes(packet[TCP].payload).decode()
		except UnicodeDecodeError as e:
			return defaultReturn
		
		isHttp = payload.startswith("POST / HTTP") or \
			payload.startswith("HTTP")
		return isHttp, payload


	def extractJsonString(self, httpPayload):
		startPos=httpPayload.find("{")
		if startPos==-1:
			return None
		return httpPayload[startPos:]


	def __call__(self, packet):
		isHttp, payload=self.isHttp(packet)
		if isHttp:
			jsonString = self.extractJsonString(payload)
			if jsonString is not None:
				try:
					jsonObject = json.loads(jsonString)
					return jsonObject
				except json.decoder.JSONDecodeError as e:
					logging.error(str(e))
					logging.error("packet dump: ")
					packet.show()
				
					return None
		return None
	
		