import time
import unittest
from datetime import datetime, timedelta

from requests.exceptions import TooManyRedirects

from decorator.decorator import CatchesTooManyRequests


class RequestsMock:
    def __init__(self):
        self.last_request = datetime.now() - timedelta(days=365)

    def evaluate_too_many_request(self):
        """
        Evaluates if the current instant is greater than the last requests by 1 second.
        """
        now = datetime.now()
        discount_second = now - timedelta(seconds=1)
        evaluate = self.last_request < discount_second
        if evaluate:
            self.last_request = now
        return evaluate

    def get(self, *args, **kwargs):
        """
        Mock endpoint.
        """
        if self.evaluate_too_many_request():
            return {'objects_list': ['motorcycle', 'car', 'truck']}
        raise TooManyRedirects


class ApiClient:
    def __init__(self):
        self.requests = RequestsMock()

    def get_objects_list(self, url):
        response = self.requests.get(url)
        return response

    @CatchesTooManyRequests
    def get_objects_list_with_decorator(self, url):
        response = self.requests.get(url)
        return response


class DecoratorTest(unittest.TestCase):

    def test_1_too_many_requests(self):
        api_client = ApiClient()

        # witch_out_decorator
        response = api_client.get_objects_list('url')
        self.assertTrue(isinstance(response, dict))
        with self.assertRaises(TooManyRedirects) as context:
            api_client.get_objects_list('url')

        # with decorator
        time.sleep(1)
        response = api_client.get_objects_list('url')
        self.assertTrue(isinstance(response, dict))
        self.assertLogs()
        response = api_client.get_objects_list_with_decorator('url')
        self.assertTrue(isinstance(response, dict))



