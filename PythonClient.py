#!/usr/bin/env python

from Publisher import *

publisher = Publisher()

# Initialize publisher with ip and port of server
publisher.init('192.168.1.2', 7711)

# Connect to server with username and password
publisher.connect('admin', 'admin')

# Define stream definition
streamDefinition = "{ 'name':'stratos_stream_definition', 'version':'1.0.0', 'payloadData':[ {'name':'message','type':'STRING'} ] }";
publisher.defineStream(streamDefinition)

# Publish sample message
publisher.publish("Test message form python client")

# Disconnect
publisher.disconnect()
