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
		return ''