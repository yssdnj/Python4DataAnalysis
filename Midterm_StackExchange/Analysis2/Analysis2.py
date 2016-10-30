import requests
import csv
import sys
import os
import json
sys.path.append(os.path.abspath('../Analysis1'))
from Analysis1_question_userid import user_ids

user_profile = {}
abs_path = os.path.abspath("../Analysis1/data")
listJsonFiles = os.listdir(abs_path)
for file in listJsonFiles:
    with open(abs_path + '/' + file) as jsonfile:
        jsonData = json.load(jsonfile)
        for item in jsonData["items"]:
            user_id = item["owner"]["user_id"]
            if not user_id in user_profile:
                user_profile[user_id] = dict((k, item["owner"][k]) for k in ("user_id", "display_name","link","reputation"))

# make requests of each user_id in user/{ids}/tags, and get tags 
user_ids_distinct = list(set(user_ids)) #425
for i in user_ids_distinct:
    userid_str = str(i)
    key = '1N2)WAQaEFzyJP*F)Al2Kw(('
    url = 'https://api.stackexchange.com/2.2/users/{}/tags?key={}\
    &order=desc&sort=popular&site=stackoverflow'.format(userid_str,key)
    r = requests.get(url)
    items = r.json()["items"]
    tags = list()
    for item in items:
        tag = item["name"]
        tags.append(tag)
    user_profile[i]['tags'] = tags   

user_profile_sorted = sorted(user_profile.items(), key = lambda item: item[1]["reputation"], reverse=True)
profile_list = [(v[1]["user_id"],v[1]["display_name"],v[1]["reputation"],
                 v[1]["tags"],v[1]["link"]) for v in user_profile_sorted]
with open('user_reputation_sorted.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["user_id", "display_name", "reputation", "tags", "link"])
    writer.writerows(profile_list)
