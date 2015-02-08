from django.core.cache import cache
from requests import get
from json import loads
from random import choice

def getAllPeople():
    #get cache
    politifact_people = cache.get('politifact_people')
    
    #test cache if None
    if politifact_people == None:
        #if None, fetch and cache All Users
        r = get('http://www.politifact.com/api/people/all/json/')
        politifact_people = loads(r.text)
        
        #TODO: filter out invalid users
        
        cache.set('politifact_people', politifact_people, None)
        
    #return cached users
    return politifact_people
    
def randomPerson():
    return choice(getAllPeople())
    
