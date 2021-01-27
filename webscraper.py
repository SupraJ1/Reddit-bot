import random
import praw
import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "<", intents=intents)

reddit = praw.Reddit(client_id = "ytPzAKfrCU_8Xw", client_secret = "qR6CPHmaA-E_OX2HQv1bnEajptG2Fw", user_agent = "Reddit Bot")

hotPost = []

hot = reddit.subreddit("ProgrammerHumor").hot(limit = 100)
for post in hot:
    hotPost.append([post.title, post.url, post.score])

@client.event
async def on_ready():
  print("INITIATION SEQUENCE COMPLETE.")

@client.command()
async def spawn(ctx):
    value = random.randint(0,100)
    embed = discord.Embed(
        title = hotPost[value][0],
        colour = discord.Colour.orange()
    )
    embed.set_footer(text = "👍 " + str(hotPost[value][2]))
    embed.set_image(url = hotPost[value][1])
    embed.set_author(name = "ProgrammerHumor")
    await ctx.send(embed = embed)

client.run("TOKEN")
