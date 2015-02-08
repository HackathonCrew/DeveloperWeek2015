import json
from sunlight_api import getImg, getID
from politifact_allpeople import randomPerson
from idol import getMouthCoordinates
from politifact_api import randomStatement

def getStatement():

    bio_id = ''
    result = {}
    count = 0

    while not bio_id or not result:

        person = randomPerson()
        first_name = person['first_name']
        last_name = person['last_name']
        name_slug = person['name_slug']
        bio_id = getID(first_name,last_name)

        if not bio_id:
            count = count + 1
            continue

        result = randomStatement(name_slug)
        count = count + 1

    image_url = getImg(bio_id)

    data = {
        'politician':'{0} {1}'.format(first_name,last_name),
        'statement':result['statement'],
        'party':result['party'],
        'image_url':image_url,
        'source_url':result['statement_url'],
        'text_offset':getMouthCoordinates(image_url),
        'hits':count
    }

    return json.dumps(data)

def getStatementMore(bio_id,first_name,last_name,name_slug):

    result = randomStatements(name_slug)


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
    parties = {'party':[
        'republican',
        'democrat'
    ]}

    return json.dumps(parties)