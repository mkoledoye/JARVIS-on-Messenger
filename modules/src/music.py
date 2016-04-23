import re
import requests

def process(input, entities):
    output = {}
    try:
        music = entities['music'][0]['value']
        #TODO: one result (limit=1) may not be the best
        r = requests.get('https://itunes.apple.com/search?term=' + music + '&limit=1&media=music')
        data = r.json()['results'][0]
        output['input'] = input
        output['output'] = data['trackName'] + '\nArtist Name: ' + data['artistName'] + '\nCollection: ' + data['collectionName'] 
        + '\nReleased: ' + data['releaseDate']
        output['success'] = True
    except:
        output['success'] = False
    return output