import json
import csv
import os
user_ids = list()
# questionids = list()
question_userid = list()
user_ques_dict = {}
ques_user_dict = {}
abs_path = os.path.abspath("../Analysis1/data")
listJsonFiles = os.listdir(abs_path)
# print(listJsonFiles)
for file in listJsonFiles:
    with open(abs_path + '/' + file) as jsonfile:
        jsonData = json.load(jsonfile)
        for item in jsonData["items"]:
            user_ids.append(item['owner']['user_id'])
            # questionids.append(item['question_id'])
            question_userid.append((item['owner']['user_id'], item['title']))
            user_ques_dict[item['owner']['user_id']] = item['title']
            ques_user_dict[item['title']] = item['owner']['user_id']

# import to other file or not 
if __name__ == '__main__':
    with open('question_userid.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["user_id", "question title"])
        writer.writerows(question_userid)
else:
    pass