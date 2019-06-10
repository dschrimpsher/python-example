import logging
import requests
from requests import RequestException
from requests_html import HTMLSession

logger = logging.getLogger('python_example')


class HttpGetException(IOError):
    """There was an ambiguous exception that occurred while handling your
    request.
    """
    def __init__(self, *args, **kwargs):
        """Initialize RequestException with `request` and `response` objects."""
        response = kwargs.pop('response', None)
        self.response = response
        self.request = kwargs.pop('request', None)
        if (response is not None and not self.request and
                hasattr(response, 'request')):
            self.request = self.response.request
        super(Exception, self).__init__(*args, **kwargs)


def client_get(server):
    try:
        session = HTMLSession()
        r = session.get(server)
        if r.status_code < 400:
            logger.info('Success %d' % r.status_code)
            logger.debug(r.html)
        else:
            logger.error('Error on Get %d' % r.status_code)
            raise HttpGetException(requests=r.request, response=r.html)
    except RequestException as e:
        logger.error('Exception %r' % e)



