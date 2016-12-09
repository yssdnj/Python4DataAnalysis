import json
import csv
import pandas as pd
# get all of the reviews of teh collected businesses. 
# In addition, add a column State to output csv file.

# get all business names from states_business.json
def get_business_names():
    names = []
    with open('../data/states_businesses.json') as f:
        businesses = json.load(f)
    for business in businesses['businesses']:
        names.append(business['name'])
    return names

# get business ids corresponding to business names
def get_all_businessID():
    business_list = []
    with open('/Users/wanlima/Documents/python/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_business.json') as businessfile:
        lines = businessfile.readlines()
        for line in lines:
            business_list.append(json.loads(line))
    df_businesses = pd.DataFrame(business_list)
    return df_businesses

# read all reviews from yelp_academic_dataset_review.json 1.95GB, which contains whole reviews from 2013-02-13 ~ 2016-07-19
def get_all_reviews():    
    reviews_list = []
    with open('/Users/wanlima/Documents/python/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json') as reviewfile:
        lines = reviewfile.readlines()
        for line in lines:
            reviews_list.append(json.loads(line))
    df_reviews = pd.DataFrame(reviews_list)
    return df_reviews

# get related DataFrame
names = get_business_names() # take short time
df_businesses = get_all_businessID() # take median time
df_reviews = get_all_reviews() # take long time

# keep the useful reviews which are under fetched businesses  
df_business_in_names = df_businesses[df_businesses['name'].apply(lambda x: x in names)]
df_reviews_of_business = df_reviews[df_reviews['business_id'].apply(lambda x: x in list(df_business_in_names['business_id']))]

df_business_in_names_temp = df_business_in_names.set_index('business_id',drop=False)
states = df_reviews_of_business['business_id'].apply(lambda busid: df_business_in_names_temp.ix[busid]['state'])
df_reviews_of_business['state'] = states

# save the reviews of fetched businesses to a csv file 
df_reviews_of_business.drop(['type'],axis=1).sort_values(by='business_id').to_csv('../data/reviews.csv',index=False)