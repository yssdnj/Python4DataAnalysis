import requests
import csv
import sys
import os
sys.path.append(os.path.abspath('../Analysis1'))
from Analysis1_question_userid import user_ids

# make requests of each user_id in user/{ids}/questions, and get items and fetch the useful data
user_down_dict = {}
user_ids_distinct = list(set(user_ids)) #425
for i in user_ids_distinct:
    userid_str = str(i)
    key = '1N2)WAQaEFzyJP*F)Al2Kw(('
    url = 'https://api.stackexchange.com/2.2/users/{}/questions?key={}\
    &pagesize=100&order=desc&sort=votes&site=stackoverflow&filter=!-*f(6pznOIfb'.format(userid_str,key)
    r = requests.get(url)
    items = r.json()["items"]
    user_down_dict[i] = 0
    for item in items:
        down_vote_count = item["down_vote_count"]
        user_down_dict[i] += down_vote_count

user_downvote_sorted = sorted(user_down_dict.items(), key = lambda item: item[1], reverse=True)
with open('downvote.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["user_id", "down_vote_count"])
    
    writer.writerows(user_downvote_sorted)