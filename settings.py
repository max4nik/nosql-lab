import os

from dotenv import load_dotenv

# loading .env vars
load_dotenv()

STRATEGY = os.environ.get('STRATEGY')
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD')
REDIS_PORT = int(os.environ.get('REDIS_PORT'))
TEST_MODE = True if os.environ.get('TEST_MODE') == 'True' else False
EVENTHUB_CONNECTION_STRING = os.environ.get('EVENTHUB_CONNECTION_STRING')
ELASTIC_PASSWORD = os.environ.get('ELASTIC_PASSWORD')
ELASTIC_CLOUD_ID = os.environ.get('ELASTIC_CLOUD_ID')
ES_INDEX = os.environ.get('ES_INDEX')
