import scrapeReddit
import discord
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = "<", intents=intents)

@client.event
async def on_ready():
  print("INITIATION SEQUENCE COMPLETE.")
  await scrapeReddit.saveHotPosts()

@client.command()
async def spawn(ctx):

    post = scrapeReddit.getHotPost()

    embed = discord.Embed(
        title = post["title"],
        colour = discord.Colour.orange()
    )
    embed.set_footer(text = "👍 " + str(post["value"))
    embed.set_image(url = post["post"])
    embed.set_author(name = post["subreddit"])
    await ctx.send(embed = embed)
    await scrapeReddit.saveHotPosts()

client.run("TOKEN")
