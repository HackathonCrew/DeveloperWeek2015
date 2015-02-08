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
        
        clean_people = []
        
        for person in politifact_people:
        
            #TODO: filter out invalid users
            first_name = person['first_name']
            last_name = person['last_name']
            name_slug = person['name_slug']

            
            print "trying " + first_name + " " + last_name
            if not first_name:
                continue
            elif not last_name:
                continue
            elif person['party']['party']=='None':
                continue
            elif person['party']['party']=='Organization':
                continue
            elif person['party']['party']=='Journalist':
                continue
            
            clean_people.append(person)
        
        cache.set('politifact_people', clean_people, None)
        
    #return cached users
    return politifact_people
    
def randomPerson():
    return choice(getAllPeople())
    
