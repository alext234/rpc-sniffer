from scapy.all import *
import json

class PacketDecoder:
	def __init__(self):
		pass
	
	
	def isHttp(self, packet):
		"""
		returns (isHttp, httpPayload)
		"""
		
		if not packet.haslayer(TCP):
			return False, None
		
		payload = bytes(packet[TCP].payload).decode()
		isHttp = payload.startswith("POST / HTTP") or \
			payload.startswith("HTTP")
		return isHttp, payload


	def extractJsonString(self, httpPayload):
		startPos=httpPayload.find("{")
		return httpPayload[startPos:]


	def __call__(self, packet):
		isHttp, payload=self.isHttp(packet)
		if isHttp:
			jsonString = self.extractJsonString(payload)
			jsonObject = json.loads(jsonString)
			return jsonObject
		return None
	
		