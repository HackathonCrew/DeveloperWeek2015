from django.test import TestCase
import json
import api.integrate_api
import api.politifact_api
import api.sunlight_api
# import getPolitifact


# Create your tests here.
class TestBasic(TestCase):
    "Basic tests"

    def test_basic(self):
        a = json.loads(api.integrate_api.getStatement())
        self.assertEqual('Michele Bachman', a['politician'])

    def test_2(self):
        a = json.loads(api.politifact_api.getPolitifact())
        self.assertEqual(a['speaker']['first_name'],'Barack')
        self.assertEqual(a['speaker']['last_name'],'Obama')

    def test_3(self):
        a = json.loads(api.politifact_api.getPolitifact())
        b = api.sunlight_api.getImg(a['speaker']['name_slug'])
        self.assertEqual(b,'www.test.com')