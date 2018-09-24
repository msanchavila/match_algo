from dotenv import find_dotenv, load_dotenv
import os
import logging
from modules import setup_logger, connect_to_neo4j
from pathlib import Path


def main():
	# connect to graph
	graph = connect_to_neo4j(
		os.getenv('NEO4J_HOST'), 
		os.getenv('NEO4J_PORT'), 
		os.getenv('NEO4J_USR'), 
		os.getenv('NEO4J_PWD'), 
	)

	logging.info('discovering cypher files...')
	cyphers = {}
	for cypher_file in Path('../data/raw/cyphers').glob('*.cypher'):
		# read cypher file
		with open(cypher_file) as fhandle:
			logging.info('reading {}.cypher'.format(cypher_file.stem))
			cyphers[cypher_file.stem] = fhandle.read()
			fhandle.close()

	logging.info('executing cypher files')
	for cypher in cyphers:
		logging.info('running cypher {}'.format(cypher))
		graph.run(cyphers[cypher])
		logging.info('complete')
	


if __name__ == "__main__":
	# load env secrets
	load_dotenv(find_dotenv())

	# setting logging
	setup_logger()

	main()