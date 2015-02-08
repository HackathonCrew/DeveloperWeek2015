from django.test import TestCase

from api import idol


# Create your tests here.
class Idol(TestCase):
    def test_getMouthCoordinates(self):
        mouthCoodinates = idol.getMouthCoordinates('http://theunitedstates.io/images/congress/450x550/P000197.jpg')
        self.assertEqual(mouthCoodinates[0], 0)
        