#!/usr/bin/env python3

import sys
import socket
import re
import ipaddress

def read_in():
	return [x.strip() for x in sys.stdin.readlines()]

def get_ip(host):
	# if host contains non-numeric, non-dot chars AND at least one dot then we can assume its a hostname. 
	try:
		return socket.gethostbyname(strip_prot(host)) if re.search("[^0-9.]", host) and re.search("\.", host) else host
	except:
		return "1.3.3.7" # silly hack. return a non-private ip if gethostbyname errors.

def strip_prot(hostname):
	# remove protocol handler
	return hostname.split("//")[1] if "//" in hostname else hostname

hosts = read_in()

for host in hosts:
	addr = get_ip(host)
	# cast addr as ipaddress type
	addr = ipaddress.ip_address(addr)
	# output if it belongs to private ip space
	if addr.is_private:
		print(host)
