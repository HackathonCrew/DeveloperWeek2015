import json
from sunlight_api import getImg, getID
from politifact_allpeople import randomPerson,getAllPeople
from idol import getMouthCoordinates
from politifact_api import randomStatement
from django.core.cache import cache

def getStatement():

    bio_id = ''
    result = {}
    count = 0
    text_offset = ''

    
    while not bio_id or not result or not text_offset:
        print 'bio_id:' + str(bio_id)
        print 'result:' + str(result)
        print 'text_offset:' + str(text_offset)
        
        person = randomPerson()
        first_name = person['first_name']
        last_name = person['last_name']
        name_slug = person['name_slug']
        bio_id = getID(first_name,last_name)
        
        if not bio_id:
            count = count + 1
            print first_name, last_name
            continue

        result = randomStatement(name_slug)
        image_url = getImg(bio_id)
        text_offset = getMouthCoordinates(image_url)
        count = count + 1


    data = {
        'politician':'{0} {1}'.format(first_name,last_name),
        'statement':result['statement'],
        'party':result['party'],
        'image_url':image_url,
        'source_url':result['statement_url'],
        'text_offset':text_offset,
        'hits':count
    }

    return json.dumps(data)

def getStatementMore(bio_id,first_name,last_name,name_slug):

    result = randomStatement(name_slug)


    image_url = getImg(bio_id)
    text_param = getMouthCoordinates(image_url)

    data = {
        'politician':'{0} {1}'.format(first_name,last_name),
        'statement':result['statement'],
        'party':result['party'],
        'image_url':image_url,
        'source_url':result['statement_url'],
        'img_width':text_param['width'],
        'img_top':text_param['top'],
        'img_height':text_param['height'],
        'img_offset':text_param['offset'],
        'img_left':text_param['left'],
    }

    return data


def getPartyArray():

    parties = cache.get('parties')

    if not parties:
        getAllPeople()
        parties = cache.get('parties')

    return parties




