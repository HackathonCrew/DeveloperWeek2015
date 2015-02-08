import json
from sunlight_api import getImg

def getStatement():
    statement = {
        'politician':'Michele Bachman',
        'statement':'If you look at Mitt Romney as the governor of Massachusetts, he\'s the only governor that put into place socialized medicine',
        'affiliation_index':0,
        'image_url':'',
        'source_url':'http://www.politifact.com/truth-o-meter/statements/2011/dec/11/michele-bachmann/michele-bachmann-says-former-mass-gov-mitt-romney-/',
        'text_offset':[0,0],
    }

    img_url = getImg('nancy-pelosi')
    statement['image_url'] = img_url

    return json.dumps(statement)


def getPartyArray():
    parties = {'party':[
        'republican',
        'democrat'
    ]}

    return json.dumps(parties)


def getStatement1():

    politician = ''

    statement = ''
    party_index = 0
    image_url = ''
    source_url = ''
    text_offset = [0,0]

    result = {
        'politician':politician,
        'statement':statement,
        'affiliation_index':party_index,
        'image_url':image_url,
        'source_url':source_url,
        'text_offset':text_offset,
    }

    return json.dumps(result)