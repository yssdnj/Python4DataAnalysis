import argparse
import requests
import twitter
import json
# from twitter import OAuth
# from requests.auth import HTTPBasicAuth
CONSUMER_KEY = 'Gfi9Gt4imoHDKNuhTqH0RvkJD'
CONSUMER_SECRET = 'YU4ukWbn8ROr1JXph9HtiXCBWh96rY0LpedN5ny8t35pLvHcgd'
ACCESS_TOKEN = '2865250744-BJcNzHyOeGcAyD8ImHyHItNPZS6Md4wXLMKyN4M'
ACCESS_SECRET = 'hZI8R5bZ4T7vlBw5ejQUv0ChabmqrmHcdteHC9csOfo1B'

api = twitter.api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_SECRET)

# oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

parser = argparse.ArgumentParser(description='here you need to enter a search term')
parser.add_argument("--search_term", help="search term")
args = parser.parse_args()
search_term = args.search_term

url = 'https://api.twitter.com/1.1/search/tweets.json?q=' + search_term

print(api.VerifyCredentials())
# print(api._RequestUrl(url,verb = 'GET'))
# r = requests.get(url)
# print(r.json())
# with open('output.txt', 'a') as f:
#         for line in api._RequestUrl(url = url, verb = 'GET'):
#             # print(type(line))
#             # f.write(json.dumps(line))
#             f.write('/n')