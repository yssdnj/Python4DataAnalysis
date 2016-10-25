import json
with open('Trump.json', 'r') as f:
        len = len(json.load(f).get('statuses'))
        print(len)