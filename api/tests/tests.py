from django.test import TestCase
import json
import api.integrate_api
import api.politifact_api
import api.sunlight_api
# import getPolitifact


# Create your tests here.
class TestBasic(TestCase):

    def test_2(self):
        a = json.loads(api.politifact_api.getPolitifact())
        self.assertEqual(a['speaker']['first_name'],'Barack')
        self.assertEqual(a['speaker']['last_name'],'Obama')

    def test_3(self):
        a = json.loads(api.integrate_api.getStatement())
        # self.assertEqual(a['image_url'],img_url)
        self.assertIsNotNone(a['image_url'])
        self.assertEqual(a['source_url'],'www.yourmom.com')
        
    def test_4(self):
        api.politifact_api.integrate_api.getStatement()