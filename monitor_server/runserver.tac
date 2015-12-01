#!/usr/bin/env python
#coding:utf-8

from twisted.internet.protocol import Protocol
from twisted.internet.protocol import Factory
from twisted.internet import reactor
from twisted.application import service,internet
import time
import operator
import json
from conf.hosts import * 

class Echo(Protocol):
        '''协议类实现用户的服务协议，例如 http,ftp,ssh 等'''
        def __init__(self, factory):
                self.factory = factory

        def connectionMade(self):
                '''连接建立时被回调的方法'''
		client = self.transport.getPeer().host
		hosts_template = send_config() 
		print "%s 已连接"%client
		if client not in hosts_template:
			print  "%s 没有加入主机监控组"%client
			self.transport.loseConnection()
		else:
			host_template = hosts_template[client]
			self.transport.write(json.dumps(host_template))
		

        def connectionLost(self, reason):
                '''连接关闭时被回调的方法'''
		client = self.transport.getPeer().host
		print "%s 已断开"%client
                #self.factory.numProtocols = self.factory.numProtocols - 1

        def dataReceived(self, data):
                '''接收数据的函数，当有数据到达时被回调'''
		client = self.transport.getPeer().host
		client_info = json.loads(data)
		client_service = client_info["service"]
		client_data = client_info["data"]
		client_timestrf = client_info["timestrf"]
		client_interval = client_info["interval"]
		client_config_all = all_config(client)
		
		client_config_info = client_config_all[client_service]
		client_config = client_config_info[0]
		if time.time() - client_timestrf < client_interval:
			if client_info["data"]["status"] == 0:
				print "%s service %s data valid"%(client,client_service)
				self.service_item_handle(client_config,client_data,client_service,client)
			else:
				print "%s service %s plugin error"%(client,client_service)
		else:
			expired_time = time.time() - client_timestrf - client_interval
			print "%s service %s data expired"%(client,client_service)
	def service_item_handle(self,client_config,client_data,client_service,client):
		for k,v in client_config.items():
			print k,client_data[k]
			oper = v["operator"]
			warning_val = v["warning"]
			critical_val = v["critical"]
			oper_func = getattr(operator,oper)

			if v["data_type"] is float:
				item_data = float(client_data[k])
				warning_res = oper_func(item_data,warning_val)
				critical_res = oper_func(item_data,critical_val)	
				print "warning:%s critical:%s"%(warning_val,critical_val)
				print "warning:%s critical:%s"%(warning_res,critical_res)

class EchoFactory(Factory):
        '''协议工厂类，当客户端建立连接的时候，创建协议对象，协议对象与客户端连接一一对应'''
        def buildProtocol(self, addr):
                return Echo(self)

if __name__ == '__builtin__':
        # 创建监听端口
	
	application = service.Application("echo")
	echoService = internet.TCPServer(8007,EchoFactory())
	echoService.setServiceParent(application) 
