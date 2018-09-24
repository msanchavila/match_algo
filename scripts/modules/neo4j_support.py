'''Modulet to support all neo4j logic'''
import logging
import os
from py2neo import Graph
from sys import exit


def connect_to_neo4j(host = "localhost", port = 7687, user = "neo4j", password = "password"):
	'''Function to connect to Neo4j'''
	logging.info('connecting to Neo4j...')
	try:
		graph = Graph(
			host = host,
			port = int(port),
			user = user, 
			password = password
		)
		logging.info('connection success')

	except Exception as e:
		logging.critical('did not connect to neo4j')
		logging.error(e)
		exit(1)

	return graph