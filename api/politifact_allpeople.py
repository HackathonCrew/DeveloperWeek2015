from django.core.cache import cache
from requests import get
from json import loads,dumps
from random import choice

def getAllPeople():
    #get cache
    politifact_people = cache.get('politifact_people')
    
    #test cache if None
    if not politifact_people:
        #if None, fetch and cache All Users
        r = get('http://www.politifact.com/api/people/all/json/')
        politifact_people = loads(r.text)
        
        clean_people = []
        parties = []
        
        for person in politifact_people:
        
            #TODO: filter out invalid users
            try:
                first_name = str(person['first_name'])
                last_name = str(person['last_name'])
                # name_slug = person['name_slug']
            except:
                continue

            
            # print "trying " + first_name + " " + last_name

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
            elif person['party']['party']=='Business leader':
                continue
            elif person['party']['party']=='Labor leader':
                continue
            elif person['party']['party']=='Activist':
                continue
            elif person['party']['party']=='Talk show host':
                continue
            elif person['party']['party']=='State official':
                continue
            elif person['party']['party']=='Columnist':
                continue
            elif person['party']['party']=='Newsmaker':
                continue
            elif person['party']['party']=='Ocean State Tea Party in Action':
                continue
            elif person['party']['party']=='Democratic Farmer-Labor':
                continue
            elif person['party']['party']=='county commissioner':
                continue
            elif person['party']['party']=='Moderate Party':
                continue

            print 'adding {0} {1}'.format(first_name,last_name)
            person = person.strip()
            clean_people.append(person)

            if person['party']['party'] not in parties:
                parties.append(person['party']['party'])

        politifact_people = clean_people
        parties = {'party': parties}
        cache.set('politifact_people', politifact_people, None)
        cache.set('parties',dumps(parties),None)
        
    #return cached users
    return politifact_people
    
def randomPerson():
    return choice(getAllPeople())
    
