import random
import praw
import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "<", intents=intents)

reddit = praw.Reddit(client_id = "ytPzAKfrCU_8Xw", client_secret = "qR6CPHmaA-E_OX2HQv1bnEajptG2Fw", user_agent = "Reddit Bot")

hotTitle = []
hotURL = []
hotScore = []
hotSubreddit = []

@client.event
async def on_ready():
  print("INITIATION SEQUENCE COMPLETE.")

@client.command()
async def spawn(ctx):

    hot = reddit.subreddit("ProgrammerHumor").hot(limit = 100)
    for post in hot:
        hotTitle.append(post.title)
        hotURL.append(post.url)
        hotScore.append(post.score)
        hotSubreddit.append(post.subreddit)


    value = random.randint(0,100)
    embed = discord.Embed(
        title = hotTitle[value],
        colour = discord.Colour.orange()
    )
    embed.set_footer(text = "👍 " + str(hotScore[value]))
    embed.set_image(url = hotURL[value])
    embed.set_author(name = hotSubreddit[value])
    await ctx.send(embed = embed)

client.run("TOKEN")
