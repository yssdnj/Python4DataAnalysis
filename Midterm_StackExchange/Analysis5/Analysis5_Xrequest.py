import json
import csv
import os

# when url_downvote is used in in Analysis1_dataFetch.py, 
# the csv files in data_downvote folder will have down_vote_count key,
# then this py file can be used
abs_path = os.path.abspath("../Analysis1/data_downvote")
listJsonFiles = os.listdir(abs_path)

user_down_dict = {}
user_id_list = list()
for file in listJsonFiles:
    with open(abs_path + '/' + file) as jsonfile:
        jsonData = json.load(jsonfile)
        for item in jsonData["items"]:
            user_id = item['owner']['user_id']
            downvote_count = item["down_vote_count"]
            user_id_list.append(user_id)
            if not user_id in user_down_dict:
                user_down_dict[user_id] = downvote_count
            else:
                user_down_dict[user_id] += downvote_count
# print(len(user_id_list))

user_downvote_sorted = sorted(user_down_dict.items(), key = lambda item: item[1], reverse=True)
with open('downvote_x.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["user_id", "down_vote_count"])
    writer.writerows(user_downvote_sorted)