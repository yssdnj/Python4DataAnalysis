# Python4DataAnalysis
Python4DataAnalysis

# Assignment_2
There are two .py files in the Assignment_2/Scripts called PythonTwitterTool_Fetch.py and Analysis.py. 
The first one is used to search and save data. The second one is used to perform relevant anyalysis.
* Step 1: use below command to fetch data with search_term and tweet_date (fetch 20 tweets each time)
```sh
python PythonTwitterTool_Fentch.py --search_date Trump --tweet_date 2016-10-24
```
```sh
python PythonTwitterTool_Fentch.py --h
usage: PythonTwitterTool_Fetch.py [-h] [--search_term SEARCH_TERM]
                                  [--tweet_date TWEET_DATE]

search tweets regarding certain term in certain created date

optional arguments:
  -h, --help            show this help message and exit
  --search_term SEARCH_TERM
                        search term
  --tweet_date TWEET_DATE
                        tweet created date in yyyy-mm-dd
```
* Step 2: use belpw coomand to show the analysis result according the data fetched via step 1
```sh
python Analysis.py --search_term Trump --min_date 2016-10-24 --max_date 2016-10-24
```
```sh
python Analysis.py --h
usage: Analysis.py [-h] [--search_term SEARCH_TERM] [--min_date MIN_DATE]
                   [--max_date MAX_DATE]

For a given search term (or across all search term) and a time window, what is
the average number of friends a user has each day.

optional arguments:
  -h, --help            show this help message and exit
  --search_term SEARCH_TERM
                        search term
  --min_date MIN_DATE   min date in yyyy-mm-dd
  --max_date MAX_DATE   max date in yyyy-mm-dd
```
Here is the sample result
![alt tag](https://github.com/yssdnj/Python4DataAnalysis/blob/master/Assignment_2/sample.png)

# Midterm_StackExchange

* Analysis1
Analysis1_dataFetch.py is used to fetch data, the data folder with 500 questions
Analysis1_question_userid.py gets the useful information from the data folder and yields the question_userid.csv file
Analysis1_badges.py fetches the badge information of user thought the user_id above and /users/{ids}, then yieldsbadges_weightage.sv file
(data_downvote folder is used for analysis5 in advance, in which files have down_vote_count feature)

* Analysis2
Analysis2.py yields user_reputation_sorted.csv file with column names of "user_id", "display_name", "reputation", "tags", “link”, and sorted by reputation descending.
Analysis2_eachTag.py yields csv file for each tag with column names of "user_id", "display_name", "reputation", “link”, also sorted by by reputation descending.

* Analysis3
Analysis3.py produces badgeType_user.csv file with column names of “badgeType”, “UserCount“, and sorted by UserCount

* Analysis4
Analysis4_1.py produces question_tags file with column names of "QuesID", "AnsCount", "Tags", “QuesTitle”.
Analysis4_2.py produces csv file for each tag with column names of “QuesID”, “AnsCount”,”QuesTitle”, and tags_summart.csv which collects the number of question and answer for each tag.

* Analysis5
Analysis_request.py fetches the down vote information for each user thought the user_id in analysis1 and /users/{ids}/questions, then yield downvote.csv file.
