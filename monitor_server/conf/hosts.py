
import templates

web_clusters = templates.linuxgenerictemplate()

web_clusters.hosts = [
		'192.168.1.11',
		]



mysql_groups = templates.linux2()

mysql_groups.hosts = [
		'192.168.1.11',
		'192.168.1.12',
		]		

monitor_group = [web_clusters,mysql_groups]


def send_config():
	host_config_dict = {}
	for group in monitor_group:
		for host in group.hosts:
			if host not in host_config_dict:
				host_config_dict[host] = {}
			for s in group.services:
				host_config_dict[host][s.name] = [s.plugin_name,s.interval]
	return host_config_dict

def all_config(client): 
	host_config_dict = {}
	for group in monitor_group:
		if client in group.hosts:
			for s in group.services:
				host_config_dict[s.name] = [s.triggers]
	return host_config_dict

