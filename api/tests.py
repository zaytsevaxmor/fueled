from django.test import TestCase
from api.models import *
from django.conf import settings
import requests, json, ast


class RestaurantTestCase(TestCase):

    auth_response = ''
    headers = {}

    def setUp(self):
        url = 'http://' + settings.TEST_PARAMS['HOST'] + '/o/token/'
        data = {'grant_type': settings.TEST_PARAMS['TOKEN']['GRANT_TYPE'], 'username': settings.TEST_PARAMS['TOKEN']['USERNAME'], 'password': settings.TEST_PARAMS['TOKEN']['PASSWORD']}
        auth = (settings.TEST_PARAMS['CLIENT']['ID'], settings.TEST_PARAMS['CLIENT']['SECRET'])
        self.auth_response = requests.post(url, data=data, auth=auth)
        # Header params
        v = ast.literal_eval(json.dumps(self.auth_response.json()))
        self.headers = {'Authorization': 'Bearer ' + v['access_token']}

    def test_get_authorization_token(self):
        self.assertEqual(self.auth_response.status_code, requests.codes.ok)

    def test_get_restaurants(self):
        url = 'http://' + settings.TEST_PARAMS['HOST'] + '/restaurants/'
        r = requests.get(url, headers = self.headers)
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_get_tracks(self):
        url = 'http://' + settings.TEST_PARAMS['HOST'] + '/tracks/'
        r = requests.get(url, headers = self.headers)
        self.assertEqual(r.status_code, requests.codes.ok)

    def test_get_reviews(self):
        url = 'http://' + settings.TEST_PARAMS['HOST'] + '/reviews/'
        r = requests.get(url, headers = self.headers)
        self.assertEqual(r.status_code, requests.codes.ok)
