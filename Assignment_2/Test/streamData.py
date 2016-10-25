# Import the necessary package to process data in JSON format
import json

# We use the file saved from last step as example
tweets_filename = 'twitter_stream_1tweet.json'
tweets_file = open(tweets_filename, "r")
tweet = json.load(tweets_file)

print(tweet['id']) # This is the tweet's id
print(tweet['created_at']) # when the tweet posted
print(tweet['text']) # content of the tweet
            
print(tweet['user']['id']) # id of the user who posted the tweet
print(tweet['user']['name']) # name of the user, e.g. "Wei Xu"
print(tweet['user']['screen_name']) # name of the user account, e.g. "cocoweixu"