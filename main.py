import os

import praw
import time

from dotenv import load_dotenv


def copy_from_source(source_subreddit):
    posts = r.subreddit(source_subreddit).hot(limit=10)

    with open('seen.txt', 'r') as f:
        seen = f.read().splitlines()
    f.close()

    for post in posts:
        if post.id not in seen:
            with open('seen.txt', 'a') as f:
                f.write(post.id + '\n')
            f.close()
            return post
        else:
            print("Already seen")


def post_to_destination(destination_subreddit, post):
    r.subreddit(destination_subreddit).submit(title=post.title, url=post.url)



def reposter(source_subreddit, destination_subreddit):
    post = copy_from_source(source_subreddit)

    if post is not None:
        print(post)
        print(post.title)
        post_to_destination(destination_subreddit, post)
    else:
        print("No new hot posts")



if __name__ == '__main__':
    load_dotenv()

    source_subreddit = os.getenv('source_subreddit')
    destination_subreddit = os.getenv('destination_subreddit')

    username = os.environ['username']
    password = os.environ['password']
    client_id = os.environ['client_id']
    secret = os.environ['secret']
    user_agent = os.environ['user_agent']

    r = praw.Reddit(
        username=username,
        password=password,
        client_id=client_id,
        client_secret=secret,
        user_agent=user_agent,
    )

    # reposter()

    # Source: https://stackoverflow.com/a/25251804/9206643
    # Schedule a job to run every minute
    starttime = time.time()
    while True:
        print("tick")
        time.sleep(3600 - ((time.time() - starttime) % 60.0))
        reposter(source_subreddit, destination_subreddit)







