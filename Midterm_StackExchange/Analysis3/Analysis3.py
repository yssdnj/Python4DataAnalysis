import requests
import csv
import sys
import os
sys.path.append(os.path.abspath('../Analysis1'))
from Analysis1_question_userid import user_ids, ques_user_dict

rows = list() # [('teacher', 34), ('python', 23), ...]
badge_No = {} # {'teacher': 34, 'python': 23, ...}
user_ids_distinct = list(set(user_ids)) #425
div = len(user_ids_distinct)//25 #425/25=17
for i in range(0,div):
    userid_str = ";".join(str(x) for x in user_ids_distinct[0+i*25:25+i*25])
    key = '1N2)WAQaEFzyJP*F)Al2Kw(('
    url = 'https://api.stackexchange.com/2.2/users/{}/badges?key={}\
    &order=desc&sort=rank&site=stackoverflow'.format(userid_str,key)
    r = requests.get(url)
    items = r.json()["items"]
    for item in items:
        badge_name = item["name"]
        # badge_userid = item["user"]["user_id"]
        if not badge_name in badge_No:
            badge_No[badge_name] = 1
        else:
            badge_No[badge_name] += 1
            
# write the sorted results into csv file
with open('badgeType_user.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["BadageType", "UserCount"])
    for k,v in badge_No.items():
        rows.append((k,v))
    # rows_2 = [(k,v) for k,v in badge_No.items()]
    rows_sorted = sorted(rows, key = lambda x: x[1],reverse=True)
    writer.writerows(rows_sorted)