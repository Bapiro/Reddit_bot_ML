import praw
from credentials import *
import json
# get reddit crediantals for the call to reddit
my_reddit = praw.Reddit(client_id=reddit_client_id,
                        client_secret=reddit_client_secret, user_agent=reddit_user_agent)

# choose subreddit and how many postsposts
sub_name = 'ifyoulikeblank'
max_posts = 10
output = []


# get the chosen amount of hot posts from subreddit
for submission in my_reddit.subreddit(sub_name).top(limit=max_posts):
    # sort the posts comments best, hot..
    # check so the comment has a body
    submission.comment_sort = 'best'
    top_comments = []
    for comment in range(10):
        if(len(submission.comments) > comment):
            if (hasattr(submission.comments[comment], "body") and submission.comments[comment].distinguished == None):
                top_comments.append(submission.comments[comment].body)
    datapost = {"id": submission.id,
                "post": submission.selftext,
                "postTitle": submission.title,
                "bestcomment": top_comments}
    output.append(datapost)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=4)
