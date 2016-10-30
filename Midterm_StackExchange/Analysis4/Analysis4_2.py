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
            preData.append((item['question_id'],item['answer_count'],item['tags'],item['title']))
# a list of tags
tags_set = set()
for pre in preData:
    for ele in pre[2]:
        tags_set.add(ele)
tags_list = list(tags_set)

# create a csv file for each tag
for tag in tags_list:
    with open(crtFold("tags") + tag + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["QuesID", "    AnsCount", "    QuesTitle"])
        rows = list()
        for pre in preData:
            if tag in pre[2]:
                rows.append((pre[0],pre[1],pre[3]))
        writer.writerows(rows)
    tag_NoQues_NoAns_dict[tag] = [len(rows),sum([x[1] for x in rows])]

with open('tags_summart.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Tag", "QuesCount", "AnsCount"])
    rows = list()
    for k,v in tag_NoQues_NoAns_dict.items():
        rows.append((k,v[0],v[1]))
    rows_sorted = sorted(rows, key = lambda x: x[1],reverse=True)
    writer.writerows(rows_sorted)