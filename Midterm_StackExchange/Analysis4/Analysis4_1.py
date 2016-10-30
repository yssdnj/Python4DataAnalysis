import json
import csv
import os

rows = list()
abs_path = os.path.abspath("../Analysis1/data")
listJsonFiles = os.listdir(abs_path)
# print(listJsonFiles)
for file in listJsonFiles:
    with open(abs_path + '/' + file) as jsonfile:
        jsonData = json.load(jsonfile)
        for item in jsonData["items"]:
            rows.append((item['question_id'],item['answer_count'],item['tags'],item['title']))
            
with open('question_tags.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["QuesID", "    AnsCount", "    Tags", "    QuesTitle"])
    writer.writerows(rows)