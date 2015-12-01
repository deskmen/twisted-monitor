#twisted-monitor

此程序用于监控任何需要监控的服务
服务端程序可以分布部署在不同地区的服务器上,客户端连接的不同地域服务端程序

#服务端需要安装twisted
pip install twisted

#添加服务端监控主机:
monitor_server/conf/hosts.py
web_clusters.hosts,mysql_groups.hosts中添加监控客户端
web_clusters.hosts = ['192.168.1.11']
mysql_groups.hosts = ['192.168.1.11','192.168.1.12']


#启动服务端:
cd monitor_server
twistd -y runserver.tac
#查看监控log:
tail -f twistd.log



#配置客户端:
monitor_client/core/heartbeat.py
self.host = '192.168.1.10'

#启动客户端:
cd monitor_client
python runserver.py start
#查看监控
tail -f runserver.log
