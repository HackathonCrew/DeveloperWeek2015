from django.test import TestCase
import views
import json

# Create your tests here.
class TestBasic(TestCase):
    "Basic tests"

    def test_basic(self):
        a = json.loads(views.getStatement())
        self.assertEqual('Michele Bachman', a['politician'])