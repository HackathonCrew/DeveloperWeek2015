import json
from sunlight_api import getImg, getID
from politifact_allpeople import randomPerson

def getStatement():

    bio_id = ''

    while not bio_id:

        person = randomPerson()
        first_name = person['first_name']
        last_name = person['last_name']
        bio_id = getID(first_name,last_name)


    image_url = getImg(bio_id)
    politician = '{0} {1}'.format(first_name,last_name)

    # statement,source_url,affiliation_index = function(name_slug)
    # text_offset = function(image_url)

    statement = 'OH HAI'
    source_url = 'www.yourmom.com'
    text_offset = [0,0]
    affiliation_index = 0


    result = {
        'politician':politician,
        'statement':statement,
        'affiliation_index':affiliation_index,
        'image_url':image_url,
        'source_url':source_url,
        'text_offset':text_offset,
    }

    return json.dumps(result)


def getPartyArray():
    parties = {'party':[
        'republican',
        'democrat'
    ]}

    return json.dumps(parties)