import json
from sunlight import congress,config
img_size = '450x550'
config.API_KEY = '16c32e40ccce456a98473e6ca3b7c718'


def getImg(person):

    img_url = ''
    bio_id = getID(person)

    if not bio_id:
        img_url = ''
    else:
        img_url = 'http://theunitedstates.io/images/congress/{0}/{1}.jpg'.format(img_size,bio_id)

    return img_url

def getID(slug):

    person = congress.legislators(last_name='Pelosi',first_name='Nancy')
    # person = congress.legislators(last_name=slug[slug.find('-')+1:],first_name=slug[0:slug.find('-')])
    if not person:
        id = ''
    else:
        person = person[0]
        id = str(person['bioguide_id'])

    return id

