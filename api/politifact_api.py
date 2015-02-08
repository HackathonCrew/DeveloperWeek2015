from json import loads
from random import choice
from requests import get

def randomStatement(name_slug):
    json_data = get('http://www.politifact.com/api/statements/truth-o-meter/people/{0}/json/?n=10'.format(name_slug))
    data = loads(json_data.text)

    #choice is a pythonic way to select a random number
    data = choice(data)
    politifact_dict = {}

    politifact_dict = {'statement_url': str(data['statement_url']), 
    'name_slug':str(data['speaker']['name_slug']), 'statement_type':str(data['statement_type']['statement_type']), 'party':str(data['speaker']['party']['party']), 'statement':str(data['statement'])}

    return politifact_dict
