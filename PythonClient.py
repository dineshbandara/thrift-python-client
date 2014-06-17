#!/usr/bin/env python

from Publisher import *

ip = '192.168.1.2'	# IP address of the server
port = 7711		# Thrift listen port of the server
username = 'admin'	# username
password = 'admin' 	# passowrd 

publisher = Publisher()

# Initialize publisher with ip and port of server
publisher.init(ip, port)

# Connect to server with username and password
publisher.connect(username, password)

# Define stream definition
streamDefinition = "{ 'name':'stratos_stream_definition', 'version':'1.0.0', 'payloadData':[ {'name':'message','type':'STRING'} ] }";
publisher.defineStream(streamDefinition)

# Publish sample message
publisher.publish("Test message form python client")

# Disconnect
publisher.disconnect()
