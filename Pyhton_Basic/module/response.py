import json
import sys
import requests

if len(sys.argv) !=2:
    sys.exit()
    
res = requests.get('https://itunes.apple.com/search?entity=song&limit=20&term=' + sys.argv[1])

o = res.json()

for i in o['results']:
    print(i['collectionName'], ":", i['collectionPrice'])