# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
CONSUMER_KEY = 'Gfi9Gt4imoHDKNuhTqH0RvkJD'
CONSUMER_SECRET = 'YU4ukWbn8ROr1JXph9HtiXCBWh96rY0LpedN5ny8t35pLvHcgd'
ACCESS_TOKEN = '2865250744-BJcNzHyOeGcAyD8ImHyHItNPZS6Md4wXLMKyN4M'
ACCESS_SECRET = 'hZI8R5bZ4T7vlBw5ejQUv0ChabmqrmHcdteHC9csOfo1B'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth,domain='userstream.twitter.com')

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.filter(track = "Trump", language = "en")

# Print each tweet in the stream to the screen 
# Here we set it to stop after getting 1000 tweets. 
# You don't have to set it to stop, but can continue running 
# the Twitter API to collect data for days or even longer. 
tweet_count = 1
file = open('twitter_stream_1tweet.json','w')
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter 
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    # print(type(json.dumps(tweet, indent = 4)))
    file.write(json.dumps(tweet, indent = 4))
    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)
       
    if tweet_count <= 0:
        break
file.close