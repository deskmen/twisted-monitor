
from services import linux


class BaseTemplate(object):
	def __init__(self):
		self.name = 'name'
		self.hosts = []
		self.services = []


class linuxgenerictemplate(BaseTemplate):
	def __init__(self):
		super(linuxgenerictemplate,self).__init__()
		self.name = "linuxcommonservices"
		self.services = [
			linux.CPU(),
			linux.LOAD(),
		]

		self.services[0].interval = 60
	
class linux2(BaseTemplate):
	def __init__(self):
		super(linux2,self).__init__()
		self.name = "linux2"
		self.services = [
			linux.CPU(),
			linux.NETWORK()
		]
