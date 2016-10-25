import argparse
import datetime
import os
import json
import statistics
from city_to_state import city_to_state_dict
from state_abb import states

# argparse
parser = argparse.ArgumentParser(description='''For a given search term (or across all search term) and a time window, 
                                                what is the average number of friends a user has each day.''')
parser.add_argument("--search_term", help="search term")
parser.add_argument("--min_date", help="min date in yyyy-mm-dd")
parser.add_argument("--max_date", help="max date in yyyy-mm-dd")
args = parser.parse_args()
search_term = args.search_term
min_day = args.min_date
max_day = args.max_date
min_date = datetime.datetime.strptime(min_day, '%Y-%m-%d').date()
max_date = datetime.datetime.strptime(max_day, '%Y-%m-%d').date()
dif_days_int = (max_date - min_date).days
today_str = datetime.datetime.now().strftime("%Y-%m-%d")
today = datetime.datetime.today().date()


def add_days(days):
    r_date = min_date + datetime.timedelta(days = days)
    r_date_str = r_date.strftime("%Y-%m-%d")
    return r_date_str

# os dir
for i in range(0,dif_days_int + 1):
    parentPath = search_term + '/' + add_days(i)
    listdir = os.listdir(parentPath)
    list_frient_count = list()
    dict_state_count = {}
    dict_state_influ_count = {}
    all_tweets = []
    for file in listdir:
        with open(parentPath + '/' + file) as f:
            content = json.load(f)
            tweets = content['statuses']
            # # data prepare for analysis 3
            all_tweets.extend(tweets)
            for tweet in tweets:
                # data prepare for analysis 1
                friends_count = tweet['user']['friends_count']
                list_frient_count.append(friends_count)
                
                # data prepare for analysis 2
                full_name = tweet['place']['full_name']
                if full_name.split(',')[1].strip() == "USA":
                    # get the state name directly e.g (Florida, USA)    
                    state_name = full_name.split(',')[0].strip()
                else:
                    # convert state abbreviations to state name. e.g for (Miami, FL), FL -> Florida
                    state_name = states[full_name.split(',')[1].strip()] 
                
                if not state_name in dict_state_count:
                    dict_state_count[state_name] = 1
                else:
                    dict_state_count[state_name] += 1

                # data prepare for analysis 4
                if not state_name in dict_state_influ_count:
                    dict_state_influ_count[state_name] = (tweet['retweet_count'] * tweet['user']['followers_count'], tweet['text'])
                else:
                    current_influ = dict_state_influ_count[state_name][0]
                    dict_state_influ_count[state_name] = (max(current_influ, tweet['retweet_count'] * tweet['user']['followers_count']),tweet['text'])
            # print(len(dict_state_count), dict_state_count)    
            # print(len(tweets))


    # analysis 1
    print('{} {}'.format(search_term, add_days(i)))
    print('Analysis 1.')
    avg_friends = int(statistics.mean(list_frient_count))
    print('avg_friends: {}'.format(avg_friends))
    
    # analysi 2
    print('Analysis 2.')
    max_state = max(dict_state_count, key=lambda k: dict_state_count[k])
    # state_sorte_reverse = sorted(dict_state_count,key = lambda state: dict_state_count[state],reverse=True)
    # print(state_sorte_reverse)
    print('{} talks most about {}: {} times'.format(max_state, search_term, dict_state_count[max_state]))

    # analysis 3. return the distinct top 10 retweeted tweets
    print('Analysis 3.')
    tweets_reverse_sorted = sorted(all_tweets,key = lambda tweet: tweet["retweet_count"],reverse=True)
    print('No.{} text: {}, retweet_count: {}'.format(1, tweets_reverse_sorted[0]['text'], tweets_reverse_sorted[0]['retweet_count']))
    tweet_count = 1
    for i in range(1,len(tweets_reverse_sorted)):
        tweet_text = tweets_reverse_sorted[i]['text'].strip('\r\n')
        tweet_text_last = tweets_reverse_sorted[i-1]['text'].strip('\r\n')
        if tweet_text != tweet_text_last:
            print('No.{} text: {}, retweet_count: {}'.format(tweet_count + 1, tweet_text, tweets_reverse_sorted[i]['retweet_count']))
            tweet_text_last = tweet_text
            tweet_count += 1
        if tweet_count == 10:
            break 

    # analysis 4
    print('Analysis 4.')
    print('most influential tweet: ')
    for k,v in dict_state_influ_count.items():
        print('{}: {}'.format(k,v[1].strip('\r\n')))
    # print(dict_state_influ_count)


    print()
    print()