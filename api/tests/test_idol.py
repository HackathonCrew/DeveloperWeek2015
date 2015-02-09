from django.test import TestCase
from json import loads
from api import idol


# Create your tests here.
class Idol(TestCase):
    
    # def test_getMouthCoordinates(self):
        # mouthCoodinates = idol.getMouthCoordinates('http://theunitedstates.io/images/congress/450x550/P000197.jpg')
        # print mouthCoodinates
        # self.assertEqual(mouthCoodinates['offset'][0], 382)
        # self.assertEqual(mouthCoodinates['offset'][1], 81)
        
        
    def test_addPersonToIdol(self):
        person = loads('{"party": {"party": "Democrat", "party_slug": "democrat"}, "first_name": "Nancy ", "last_name": "Pelosi", "name_slug": "nancy-pelosi", "canonical_photo": "http://static.politifact.com.s3.amazonaws.com:80/mugs%2Fmug-nancypelosi.jpg"}')
            
        idol.addPersonToIdol(person)
        
    # def test_addDocument(TestCase):
        # statements = [ {'statement': 'hi1', 'url': 'http://1'}, {'statement': 'hi2', 'url': 'http://2'},  ]
        # idol.addDocumentToIdol(statements, 'test-politician')
        
    # def test_findRelatedStatements(TestCase):
        # print idol.findRelatedStatements('Nancy  Pelosi')
        
        
    # def test_randomKey(TextCase):
        # idol.getRandomIdolPerson()
        
    # def test_getIdolPerson(TestCase):
        # print idol.getRandomIdolPerson()