import requests


def getMouthCoordinates(url):
    r = requests.get(
        'https://api.idolondemand.com/1/api/sync/detectfaces/v1',
        params = {
            'apikey': '31379774-e946-4bff-b26e-35e93ea7a67e',
            'url' : url,
        })
    print r.text
    
    return (0,0)
    