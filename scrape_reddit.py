import praw
from random import choice

reddit = praw.Reddit(client_id = "ytPzAKfrCU_8Xw", client_secret = "qR6CPHmaA-E_OX2HQv1bnEajptG2Fw", user_agent = "Reddit Bot")

hotPosts = []

async def saveHotPosts(subreddits):
    hot = reddit.subreddit(choice(subreddits)).hot(limit = 100)
    for post in hot:
        hotPosts.append({"title": post.title, "post": post.url, "score": post.score, "subreddit": post.subreddit})

async def getHotPost():
    return choice(hotPosts)
