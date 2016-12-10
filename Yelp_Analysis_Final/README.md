# Yelp Data Analysis

## Dataset 
### [Yelp Fusion API (v3)](https://www.yelp.com/developers/documentation/v3/get_started):

#### Usage
Currently, most yelp developer are using [Yelp 2.0](https://github.com/Yelp/yelp-python/blob/master/README.md). Bu now there is a new version API called [Yelp Fusion](https://github.com/Yelp/yelp-fusion) published 
in September 20, 2016 via [Yelp Blog](https://www.yelpblog.com/2016/09/yelp-fusion-developer-program-data-api-access)
```
    with open("client_info.json") as cred:
        data = json.load(cred)
    token = requests.post('https://api.yelp.com/oauth2/token', data=client_app)
    access_token = token.json()['access_token']
```
```
    headers = {'Authorization': 'bearer %s' % access_token}
    url = 'https://api.yelp.com/v3/businesses/search'
    params = {
        'location': "MA",
        'limit': 20
    }
resp = requests.get(url=url, params=params, headers=headers)
```

#### Notes on the Dataset
business
![business](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/business.png)

### [Yelp Dataset Challenge](https://www.yelp.com/dataset_challenge)
Due to the limitation and incompletion of Yelp Fusion API, developer can only fetch 3 reviews for each business and can not fetch user information, So I use [Yelp Dataset Challenge](https://www.yelp.com/dataset_challenge) as an auxiliary dataset.

The Challenge Dataset:
  - 2.7M reviews and 649K tips by 687K users for 86K businesses
  - 566K business attributes, e.g., hours, parking availability, ambience.
  - Social network of 687K users for a total of 4.2M social edges.
  - Aggregated check-ins over time for each of the 86K businesses
  - 200,000 pictures from the included businesses

Cities:
  - U.K.: Edinburgh
  - Germany: Karlsruhe
  - Canada: Montreal and Waterloo
  - U.S.: Pittsburgh, Charlotte, Urbana-Champaign, Phoenix, Las Vegas, Madison
 
In this Analysis, mainly focus on reviews, users and business in U.S cities

#### Notes on the Dataset
review & user
![reviewanduser](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/review%26user.png)

## Analysis

### 1. Stars & Price -- States

#### Questions
  - Consumption level in each state
  - Average Rate in each state
  - Average Rate in each price level
  - Percentage of each price level

#### Date table
![df_price_avgRate](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis1/df_price_avgRate.png)
![df_state_avgRate](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis1/df_state_avgRate.png)
![df_state_pricelevel](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis1/df_state_pricelevel.png)

#### Analysis
> The consumption level can infer from the amount of $ and $$$$ businesses.
NY (New York) and NV (Nevada) have the most number of $$$$ businesses，which is same as common sense

> Plot 2 shows the  Average Rate in each state and the horizontal red line is the U.S average rate.
We can easily know which state is above averate level and which state is below.

> the connection between Average rate and business price level. It shows $$$$ businesses have the highest
avgerage rate and $$ businesses have the lowest. However, the difference  between each price level is very small.
So the conclusion is price level makes a small influence on average rate.

> $\$ businesses occupy more than half of whole busienss, and $$$$ businesses only occupy 1.2%.  

#### Visualization
 ![Analysis1](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis1.png)
 
### 2. Connect register User & Review Count

#### Question
  - Relationship between register User Count and Review Count in each month

#### Date table
![df_analysis2](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis2/df_analysis2.png)

#### Aanalysis
> According to the plot, We can easily find that new user count and review count follow the same trend before 2015. 
After 2015, new user count becomes falling down and review count still rise.

>Speculation: The review count will keep going up (Ignore the last motnth falling, because there is incomplete
review collection in last month). The new user count will keep in a almost smooth level monthly, because the peak 
moment has passed and yelp is stepping into a normal age.

> An interesting phenomenon, all of the peaks occur in the middle of year for both new user count and review count.
This can be a further research.

#### Visualization
 ![Analysis2](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis2.png)
 ![Analysis2_zoon](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis2_zoom2.png)
 
### 3. Yelp User Analysis

#### Questions
  - Ranking of User review votes
  - Comparison amonge each kind of votes

#### Date table
![df_analysis3](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis3/df_analysis3.png)

#### Analysis
> The ranking is based on total votes. Harald is No.1 in all three kinds of votes (funny, cool and useful).
> Among these three kinds of votes,  useful vote is always the highest, so it is the most significant, then cool and funny. 

#### Visualization
 ![Analysis3](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis3.png)
 
### 4. Business Classification

#### Questions
  - What kind of categories are there in the yelp business
  - Percentage of each category
  - What subclass does a certain category have

#### Date table
![df_categories](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis4/df_categories.png)
![df_restaurant](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis4/df_restaurant.png)

#### Analysis
> According to the pie char, We can find almost a quarter are Restaurant businesses, then Shopping and food. 
Here is how Yelp classify business in details. [Yelp Category List](https://www.yelp.com/developers/documentation/v3/all_category_list)

> Among restaurants businesses, Mexican cuisine is most popular in USA, then Italian and Chinese food.
In other side, from the restaurant composition, we can infer the population composition in U.S.

#### Visualization
 ![Analysis4](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis4.png)
 
### 5. Simple Search Engine

#### Question
  - If I wanna to have Brunch in Pittsburgh, How can I fand a nice restaurant

#### Date table
![analysis5_Pitsburgh_Brunch](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis5/analysis5_Pitsburgh_Brunch.csv)

#### Analysis
> This is a simple Search Engine for Pittsburgh, Charlotte, Urbana-Champaign, Phoenix, Las Vegas, Madison. 
User can enter City name and business Category, Then a plot will show the business ranking for that kind category in that city with business total score(Average rate * review count) and top five business addresses.

#### Visualization
 ![Analysis5](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Yelp_Analysis_Final/output/analysis5.png)
 
## Author

* **Wanli Ma** 

## Acknowledgments

* Spandan Brahmbhattd

