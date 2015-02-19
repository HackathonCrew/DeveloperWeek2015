import requests
from json import loads,dumps
from api import politifact_allpeople
from api import politifact_api
from api import sunlight_api

def getMouthCoordinates(url):
    r = requests.get(
        'https://api.idolondemand.com/1/api/sync/detectfaces/v1',
        params = {
            'apikey': '31379774-e946-4bff-b26e-35e93ea7a67e',
            'url' : url,
        })
    try:
        face = loads(r.text)['face'][0]
        face['offset'] = face['left'] + face['width'], int(face['height'] * .3)
    except:
        return ''

    return face
    
def addTextToIdol():

    allPeople = politifact_allpeople.getAllPeople()
    count = 0
    
    for person in allPeople:
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

        id = sunlight_api.getID(first_name,last_name)

        if id:
            result = politifact_api.randomStatements(name_slug)
            if not result:
                continue
            image_url = sunlight_api.getImg(id)
            text_param = getMouthCoordinates(image_url)

            data = {
            
                'reference':id,
                'title':'{0} {1}'.format(first_name,last_name),
                #parametric field
                'politician':'{0} {1}'.format(first_name,last_name),
                #index field
                'statement':result['statement'],
                
                #extra json
                'party':result['party'],
                'image_url':image_url,
                'source_url':result['statement_url'],
                'img_width':text_param['width'],
                'img_top':text_param['top'],
                'img_height':text_param['height'],
                'img_offset':text_param['offset'],
                'img_left':text_param['left'],
                
            }
            json = dumps({ 'document': [ data ] })
            try:
                print "------------------->found match"
                requests.get("https://api.idolondemand.com/1/api/sync/addtotextindex/v1", 
                params = 
                    {
                        'apikey': '31379774-e946-4bff-b26e-35e93ea7a67e',
                        'json': dumps({ 'document': [ data ] }),
                        'index': 'politicians'
                    })
                count+=1
            except (e):
                print error
                print e