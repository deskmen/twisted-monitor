#!/usr/bin/env python

import socket
import json
import time
import threading
from core.heartbeat import * 
from plugins import plugin_api


class MonitorClient(object):
    def __init__(self):
        self.sgin = connection_server()
        self.host_config = self.sgin.client_config()
        print self.host_config
    def start(self):
        self.handle() 
    def get_host_config(self):
        pass
    def handle(self):
        if self.host_config:
            while 1:
                for service,val in self.host_config.items():
                    if len(val) < 3:
                        self.host_config[service].append(0)
                    plugin_name,interval,last_run_timestrf = val
                    now_time_strftime = time.time()
                    last_time = now_time_strftime - last_run_timestrf 
                    if last_time < interval:
                        next_run_time = interval - last_time 
                        print "service %s next run time %s"%(service,next_run_time)
                    else:
                        print "going to run the %s again"%service
                        self.host_config[service][2] = time.time() 
                        t = threading.Thread(target=self.call_plugin,args=(service,plugin_name,interval))
                        t.start()
                time.sleep(1)
        else:
            print "cannot get host config"
    def call_plugin(self,service,plugin_name,interval):
        func = getattr(plugin_api,plugin_name)
        report_data = {
            'service':service,
            'data':func(),
            'timestrf':time.time(),
            'interval':interval
        }
        r_data = json.dumps(report_data)
        self.sgin.send_data(r_data)
