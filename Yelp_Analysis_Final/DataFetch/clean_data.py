import json
import csv
import pandas as pd

def get_all_businessID():
    business_list = []
    with open('/Users/wanlima/Documents/python/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json') as businessfile:
        lines = businessfile.readlines()
        for line in lines:
            business_list.append(json.loads(line))
    df_businesses = pd.DataFrame(business_list)
    return df_businesses

def get_all_users():
    users_list = []
    with open('/Users/wanlima/Documents/python/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_user.json') as userfile:
        lines = userfile.readlines()
        for line in lines:
            users_list.append(json.loads(line))
    df_users = pd.DataFrame(users_list)
    return df_users

def get_all_reviews():    
    reviews_list = []
    with open('/Users/wanlima/Documents/python/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json') as reviewfile:
        lines = reviewfile.readlines()
        for line in lines:
            reviews_list.append(json.loads(line))
    df_reviews = pd.DataFrame(reviews_list)
    return df_reviews

# business
df_businesses = get_all_businessID() # take median time
states = ['PA','NC','WI','IL','NV','AZ'] # only focus on these 6 states
df_business_six = df_businesses[df_businesses['state'].apply(lambda x: x in states)]
ids = list(df_business_six['business_id'])
df_business_six.drop(['type','hours','latitude','longitude','neighborhoods'], axis=1).to_csv('../data/business.csv', index=False)

# user
df_users = get_all_users()
df_users.drop(['type'], axis=1).to_csv('../data/user.csv', index=False)

# review
df_reviews = get_all_reviews()
df_reviews_of_business = df_reviews[df_reviews['business_id'].apply(lambda x: x in ids)]
df_reviews_of_business.drop(['type','text'],axis=1).sort_values(by='business_id').to_csv('../data/reviews.csv', index=False)
