from django.test import TestCase

from django.core.cache import cache
from api import politifact_allpeople
# import getPolitifact


# Create your tests here.
class Politifact_AllPeople(TestCase):
    "Basic tests"

    #def test_cache(self):
    
    
    def test_random(self):
        cache.set('politifact_people', [{'name_slug': 'name'}], None)
        allPeople = cache.get('politifact_people')
        randomPerson = politifact_allpeople.randomPerson()
        self.assertEqual(allPeople[0]['name_slug'], randomPerson['name_slug'])
