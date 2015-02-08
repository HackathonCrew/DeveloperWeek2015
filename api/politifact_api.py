from json import loads
from random import choice
from requests import get
from html2text import html2text

def randomStatement(name_slug):
    json_data = get('http://www.politifact.com/api/statements/truth-o-meter/people/{0}/json/?n=100'.format(name_slug))
    data = loads(json_data.text)

    #remove statements that were not stated by this person
    for i,each in enumerate(data):
        if data[i]['speaker']['name_slug'] != name_slug:
            data.remove(each)

    if len(data) == 0:
        return {}

    #choice is a pythonic way to select a random number
    data = choice(data)
    statement = cleanStatement((data['statement']))

    politifact_dict = {'statement_url': str(data['statement_url']), 
    'name_slug':str(data['speaker']['name_slug']), 'statement_type':str(data['statement_type']['statement_type']), 'party':str(data['speaker']['party']['party']), 'statement':statement}

    return politifact_dict

def randomStatements(name_slug,n):
    json_data = get('http://www.politifact.com/api/statements/truth-o-meter/people/{0}/json/?n={1}'.format(name_slug,n))
    data = loads(json_data.text)
    statements = []
    statement_urls = []
    statementArray = []
    for each in data:
        statement = cleanStatement(each['statement'])
        # statements.append(statement)
        statement_url = (each['statement_url'])
        statementArray.append({'statement':statement, 'url':statement_url})

    return statementArray

def cleanStatement(a):
    statement = html2text(a)

    while 1:
        index = statement.find('\n')
        if index < 0:
            break
        statement = statement[0:index] + ' ' + statement[index+1:]

    while 1:
        index = statement.find('\"')
        if index < 0:
            break
        statement = statement[0:index] + ' ' + statement[index+1:]

    return statement




