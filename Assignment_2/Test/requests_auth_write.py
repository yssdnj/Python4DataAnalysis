import argparse
import requests
import twitter
import json
from requests_oauthlib import OAuth1
CONSUMER_KEY = 'Gfi9Gt4imoHDKNuhTqH0RvkJD'
CONSUMER_SECRET = 'YU4ukWbn8ROr1JXph9HtiXCBWh96rY0LpedN5ny8t35pLvHcgd'
ACCESS_TOKEN = '2865250744-BJcNzHyOeGcAyD8ImHyHItNPZS6Md4wXLMKyN4M'
ACCESS_SECRET = 'hZI8R5bZ4T7vlBw5ejQUv0ChabmqrmHcdteHC9csOfo1B'

auth = OAuth1(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_TOKEN,ACCESS_SECRET)

parser = argparse.ArgumentParser(description='here you need to enter a search term')
parser.add_argument("--search_term", help="search term")
args = parser.parse_args()
search_term = args.search_term
url = "https://api.twitter.com/1.1/search/tweets.json?q=" + search_term + "&until=" + "2016-10-23" + "&count=100&"
r = requests.get(url,auth=auth)
# print(r.text)
# print(r.json())
headType = r.headers['content-type']
# print(headType)
print(type(json.dumps(r.json(),indent = 4)))
with open(search_term + '.json', 'w') as f:
        # for line in r.json():
            # print(type(line))
        f.write(json.dumps(r.json(),indent = 4))
        type(f.readline)

