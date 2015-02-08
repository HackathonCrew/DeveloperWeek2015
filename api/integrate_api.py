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


def getPartyArray():
    parties = {'party':[
        'republican',
        'democrat'
    ]}

    return json.dumps(parties)