import json
from sunlight import congress,config
img_size = '450x550'
config.API_KEY = '16c32e40ccce456a98473e6ca3b7c718'


def getImg(bio_id):

    # img_url = ''
    # bio_id = getID(first_name,last_name)
    #
    # if not bio_id:
    #     img_url = ''
    # else:
    img_url = 'http://theunitedstates.io/images/congress/{0}/{1}.jpg'.format(img_size,bio_id)

    return img_url

def getID(first_name,last_name):

    person = congress.legislators(last_name=last_name,first_name=first_name)
    if not person:
        id = ''
    else:
        person = person[0]
        id = str(person['bioguide_id'])

    return id

