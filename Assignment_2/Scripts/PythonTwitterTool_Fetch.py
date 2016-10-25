import argparse
import json
import os
import datetime
from twitter import Twitter, OAuth

# OAuth
CONSUMER_KEY = 'Gfi9Gt4imoHDKNuhTqH0RvkJD'
CONSUMER_SECRET = 'YU4ukWbn8ROr1JXph9HtiXCBWh96rY0LpedN5ny8t35pLvHcgd'
ACCESS_TOKEN = '2865250744-BJcNzHyOeGcAyD8ImHyHItNPZS6Md4wXLMKyN4M'
ACCESS_SECRET = 'hZI8R5bZ4T7vlBw5ejQUv0ChabmqrmHcdteHC9csOfo1B'
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_searchApi= Twitter(auth=oauth)

# argparse
parser = argparse.ArgumentParser(description='search tweets regarding certain term in certain created date')
parser.add_argument("--search_term", help="search term")
parser.add_argument("--tweet_date", help="tweet created date in yyyy-mm-dd")
args = parser.parse_args()
search_term = args.search_term
tweet_date_str = args.tweet_date
tweet_date = datetime.datetime.strptime(tweet_date_str, '%Y-%m-%d').date()

# since_date = tweet_date - datetime.timedelta(days = 1)
# since_date_str = since_date.strftime("%Y-%m-%d")
until_date = tweet_date + datetime.timedelta(days =1 )
until_date_str = until_date.strftime("%Y-%m-%d")

today_str = datetime.datetime.now().strftime("%Y-%m-%d")
today = datetime.datetime.today().date()
today_back_oneWeek = today - datetime.timedelta(days = 8)
today_back_oneWeek_str = today_back_oneWeek.strftime("%Y-%m-%d")

# functions
def createFolder(folderName):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    dateTime = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = folderName + '/' + tweet_date_str
    isExists=os.path.exists(path)
    if(not isExists):
        os.makedirs(path)
    return path + '/'  + dateTime

# fetch data 
# result = twitter_searchApi.geo.search(query="USA", granularity="country")
# place_id = result['result']['places'][0]['id']
place_id = '96683cc9126741d1'
iterator = twitter_searchApi.search.tweets(q = search_term + '&place:96683cc9126741d1', since = tweet_date_str, until = until_date_str, lang = 'en',count=100)
test = twitter_searchApi.search.tweets(q='#nlproc&place:96683cc9126741d1', result_type='recent', lang='en', count=100)
path = createFolder(search_term)
with open(path + '.json', 'w') as f:
    f.write(json.dumps(iterator, indent = 4))



