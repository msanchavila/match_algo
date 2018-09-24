'''Modules to support creatings logs'''
import os
import yaml
import logging.config
import logging


def setup_logger(default_path='logging.yaml', default_level=logging.INFO, env_key='LOG_CFG'):
    ''' Function to setup logging system

	Args:
		default_path <str>: location for logging configuration
		default_level <logging.level>: logging level DEBUG, INFO, WARNING, ERROR, CRITICAL
		env_key <str>: secret logging location
    '''
    path = default_path
    value = os.getenv(env_key, None)

    if value:
        path = value

    if os.path.exists(path):
        with open(path, 'rt') as f:
            try:
                config = yaml.safe_load(f.read())
                logging.config.dictConfig(config)

            except Exception as e:
                print(e)
                print('Error in Logging Configuration. Using default configs')
                logging.basicConfig(level=default_level)
    else:
        logging.basicConfig(level=default_level)
        print('Failed to load configuration file. Using default configs')