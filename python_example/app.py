from time import sleep
import logging
from python_example import http_client

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('python_example')


def run():
    while True:
        sleep(1)
        http_client.client_get('http://example.com')


if __name__ == '__main__':
    logger.info('Starting Client App')
    run()

