from django.test import TestCase
from django.conf import settings
import requests, json, ast
import datetime, random


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

    def test_create_restaurant(self):
        url = 'http://' + settings.TEST_PARAMS['HOST'] + '/restaurants/'
        # Test data
        name = 'Restaurant ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        desc = 'Desc ' + str(random.randint(10, 100000))
        addr = 'Novosibirsk, Injenernaya street, 4a'
        data = {'name': name, 'description': desc, 'address': addr}
        r = requests.post(url, data=data, headers=self.headers)
        self.assertEqual(r.status_code, requests.codes.created)

    def test_create_review(self):
        url = 'http://' + settings.TEST_PARAMS['HOST'] + '/reviews/'
        # Test data
        states = ['good', 'bad', 'so-so', 'excelent']
        ind = random.randint(0, len(states) - 1)
        text = 'My ' + states[ind] + ' review of ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        creator = 2
        restaurant = 1
        data = {'text': text, 'creator': creator, 'restaurant': restaurant}
        r = requests.post(url, data=data, headers=self.headers)
        self.assertEqual(r.status_code, requests.codes.created)

    def test_create_track(self):
        url = 'http://' + settings.TEST_PARAMS['HOST'] + '/tracks/'
        # Test data
        creator = 2
        restaurant = 1
        data = {'creator': creator, 'restaurant': restaurant}
        r = requests.post(url, data=data, headers=self.headers)
        self.assertEqual(r.status_code, requests.codes.created)
