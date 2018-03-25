from rpcsniffer import Config

class OutputFormatter:
	
	def __init__(self):
		pass
	
	def columnTitles(self):
		return "id".ljust(Config.ID_SIZE) +\
			"method".ljust(Config.METHOD_SIZE) + \
			"params".ljust(Config.PARAMS_SIZE) + \
			"result".ljust(Config.RESULT_SIZE) 

	def __call__(self, jsonObject):
		if 'method' in jsonObject:
			return \
				str(jsonObject['id']).ljust(Config.ID_SIZE) + \
				jsonObject['method'].ljust(Config.METHOD_SIZE) + \
				str(jsonObject['params']).ljust(Config.PARAMS_SIZE)
		elif 'result' in jsonObject:
			return str(jsonObject['id']).ljust(Config.ID_SIZE) + \
			' '.ljust(Config.METHOD_SIZE) + \
			' '.ljust(Config.PARAMS_SIZE) + \
			str(jsonObject['result']).ljust(Config.RESULT_SIZE)
					
		return ''