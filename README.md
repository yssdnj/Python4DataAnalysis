# Python4DataAnalysis
Python4DataAnalysis

# Assignment_2
There are two .py files in the Assignment_2/Scripts called PythonTwitterTool_Fetch.py and Analysis.py. 
The first one is used to search and save data. The second one is used to perform relevant anyalysis.
* Step 1: use below command to fetch data with search_term and tweet_date
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
