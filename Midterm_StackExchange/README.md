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
