import json
from sunlight import congress,config
# img_size = '450x550'
img_size = '225x275'
config.API_KEY = '9336ef88e8d1490c826c340876470519'


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
    print "------------------------"
    print first_name, last_name
    person = congress.legislators(last_name=last_name,first_name=first_name)
    print person
    if not person:
        print '--------------->not a person'
        id = ''
    else:
        print '----------------is a person'
        person = person[0]
        id = str(person['bioguide_id'])
        exit()

    return id

