from generic import BaseService

class CPU(BaseService):
	def __init__(self):
		super(CPU,self).__init__()
		self.interval = 30
		self.name = "linux_cpu"
		self.plugin_name = "get_cpu_status"
		self.triggers = {
			'idle':{
				'func':'avg',
				'last':10*60,
				'count':1,
				'operator':'lt',
				'warning':40,
				'critical':30,
				"data_type":float
			},
			'iowait':{
				'func':'hit',
				'last':10*60,
				'count':5,
				'operator':'gt',
				'warning':30,
				'critical':40,
				'data_type':float
			}
		}

class LOAD(BaseService):
        def __init__(self):
                super(LOAD,self).__init__()
                self.interval = 30
                self.name = "linux_load"
                self.plugin_name = "get_load_status"
                self.triggers = {
                        'load1':{
                                'func':'hit',
                                'last':10*60,
                                'count':1,
                                'operator':'gt',
                                'warning':5,
                                'critical':10,
                                "data_type":float
                        },
                        'load5':{
                                'func':'hit',
                                'last':10*60,
                                'count':1,
                                'operator':'gt',
                                'warning':1,
                                'critical':10,
                                'data_type':float
                        },
			'load15':{
                                'func':'hit',
                                'last':10*60,
                                'count':1,
                                'operator':'gt',
                                'warning':5,
                                'critical':10,
                                'data_type':float
                        } 
			
                }


class MEMORY(BaseService):
	def __init__(self):
        	super(MEMORY,self).__init__()
        	self.interval = 20
        	self.name = "linux_memory"
        	self.plugin_name = "get_memory_status"
        	self.triggers = {
        		'usage':{
        			'func':'avg',
        			'last':5*60,
				'count':1,
        			'operator':'gt',
        			'warning':80,
        			'critical':90,
				'data_type':float
        		}
        	}


class NETWORK(BaseService):
	def __init__(self):
        	super(NETWORK,self).__init__()
        	self.interval = 60 
        	self.name = "linux_network"
        	self.plugin_name = "get_network_status"
        	self.triggers = {
        		'in':{
        			'func':'hit',
        			'last':10*60,
				'count':5,
        			'operator':'gt',
        			'warning':1024*1024*10,
        			'critical':1024*1024*15,
				'data_type':float	
        		},
        		'out':{
        			'func':'hit',
        			'last':10*60,
				'count':5,
        			'operator':'gt',
        			'warning':1024*1024*10,
        			'critical':1024*1024*15,
				'data_type':float
        		}
        	}
