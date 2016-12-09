import requests
import json
import os
from requests_oauthlib import OAuth1
from state_abb import states_list

# read API keys
def obtain_bearer_token():
    with open("client_info.json") as cred:
        data = json.load(cred)
    token = requests.post('https://api.yelp.com/oauth2/token', data=data)
    access_token = token.json()['access_token']
    return access_token

def createFolder(folderName):  
    path = folderName + '/'
    isExists=os.path.exists(path)
    if(not isExists):
        os.makedirs(path)
    return path

def dataFetch_state_size(state, size):
    access_token = obtain_bearer_token()
    headers = {'Authorization': 'bearer %s' % access_token}
    state_businesses_dict = {'businesses':[]}
    access_token = obtain_bearer_token()
    for i in range(0, size):
        url = 'https://api.yelp.com/v3/businesses/search'
        params = {
            'location': state,
            'limit': 20,
            'offset': i*20
        }
        resp = requests.get(url=url, params=params, headers=headers) 
        state_businesses_dict['businesses'] = state_businesses_dict['businesses'] + resp.json()['businesses']
    return state_businesses_dict

def save_json(states_list,size):
    data_total = {'businesses':[]}

    # save each state business data into its owen json file
    for state in states_list:
        temp_data = dataFetch_state_size(state, size)
        with open(createFolder('../data/analysis1_data/States') + state + '.json', 'w') as f:
            f.write(json.dumps(temp_data, indent = 4))
        data_total['businesses'] = data_total['businesses'] + temp_data['businesses']

    # save all states business data into one json file 
    with open(createFolder('../data/analysis1_data/States') + 'states_businesses.json', 'w') as f:
            f.write(json.dumps(data_total,indent = 4))

save_json(states_list,50) # 50*20 each state, 1000*51 = 51000 businesses (51000-434 =50566)