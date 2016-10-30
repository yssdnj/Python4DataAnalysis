import requests
import csv
from Analysis1_question_userid import user_ids, ques_user_dict

bronze = 0 
silver = 0
gold = 0
rows = list()
user_badge_dict={}
user_ids_distinct = list(set(user_ids))
div = len(user_ids_distinct)//25
for i in range(0,div):
    userid_str = ";".join(str(x) for x in user_ids_distinct[0+i*25:25+i*25])
    key = '1N2)WAQaEFzyJP*F)Al2Kw(('
    url = 'http://api.stackexchange.com/2.2/users/{}?key={}\
    &order=desc&sort=reputation&site=stackoverflow'.format(userid_str,key)
    r = requests.get(url)
    items = r.json()["items"]
    for item in items:
        user_id = item["user_id"]
        user_bronze = item["badge_counts"]["bronze"]
        user_silver = item["badge_counts"]["silver"]
        user_gold = item["badge_counts"]["gold"]
        user_badge_dict[user_id]= [user_bronze, user_silver, user_gold]
        bronze += user_bronze
        silver += user_silver
        gold += user_gold

# write the sorted results into csv file
with open('badges_weightage.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["user_id", "weightage", "bronze", "silver", "gold", "question title"])

    for ques,user_id in ques_user_dict.items():
        u_bronze = user_badge_dict[user_id][0]
        u_silver = user_badge_dict[user_id][1]
        u_gold = user_badge_dict[user_id][2]
        rows.append((user_id, float(format(u_bronze/bronze + u_silver/silver + u_gold/gold,'.6f')),
                        u_bronze, u_silver, u_gold, ques))
    rows_sorted = sorted(rows, key = lambda x: x[1],reverse=True)
    writer.writerows(rows_sorted)
    print(len(rows_sorted))