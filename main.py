import praw
from credentials import *

my_reddit = praw.Reddit(client_id=reddit_client_id,
                        client_secret=reddit_client_secret, user_agent=reddit_user_agent)

sub_name = 'askreddit'
max_posts = 10

for submission in my_reddit.subreddit(sub_name).hot(limit=max_posts):
    print("---")
    print("title:" + submission.title)
    submission.comment_sort = 'best'
    comment_body = [comment.body for comment in submission.comments if (
        hasattr(comment, "body") and comment.distinguished == None)][0]
    top_comment = comment_body
    print("-" + top_comment)
