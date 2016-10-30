import json
import csv
import os

def crtFold(folder):
    path = folder + '/'
    isExists=os.path.exists(path)
    if(not isExists):
        os.mkdir(path)
    return path

preData = list()
tag_NoQues_NoAns_dict = {}
abs_path = os.path.abspath("../Analysis1/data")
listJsonFiles = os.listdir(abs_path)
for file in listJsonFiles:
    with open(abs_path + '/' + file) as jsonfile:
        jsonData = json.load(jsonfile)
        for item in jsonData["items"]:
            preData.append((item['tags'],item['owner']["user_id"], item['owner']["display_name"],item['owner']['reputation'],item['owner']["link"]))
# a list of tags
tags_set = set()
for pre in preData:
    for ele in pre[0]:
        tags_set.add(ele)
tags_list = list(tags_set)

# create a csv file for each tag
for tag in tags_list:
    with open(crtFold("tags") + tag + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["user_id", "display_name", "reputation", "link"])
        rows = list()
        for pre in preData:
            if tag in pre[0]:
                rows.append((pre[1],pre[2],pre[3],pre[4]))
        rows_sorted = sorted(rows, key = lambda x: x[2], reverse=True)
        writer.writerows(rows_sorted)
