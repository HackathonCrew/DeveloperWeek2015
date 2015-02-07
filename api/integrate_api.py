import json

def getStatement():
    statement = {
        'politician':'Michele Bachman',
        'statement':'If you look at Mitt Romney as the governor of Massachusetts, he\'s the only governor that put into place socialized medicine',
        'affiliation_index':0,
        'image_url':'http://thedailybanter.com/wp-content/uploads/2013/10/Screen-Shot-2013-10-07-at-4.19.43-PM.png',
        'source_url':'http://www.politifact.com/truth-o-meter/statements/2011/dec/11/michele-bachmann/michele-bachmann-says-former-mass-gov-mitt-romney-/',
        'text_offset':0,
    }

    return json.dumps(statement)


def getPartyArray():
    parties = [
        'republican',
        'democrat'
    ]

    return json.dumps(parties)