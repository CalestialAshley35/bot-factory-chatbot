import discord
from discord.ext import commands

# Define the intents
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# Create the bot instance with the defined intents
bot = commands.Bot(command_prefix='!', intents=intents)
bot_token = None  # Initialize bot_token variable globally

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello! I am your friendly AI bot.')

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000  # in milliseconds
    await ctx.send(f'Pong! Latency is {latency:.2f}ms.')

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Bot Information", description="I am a friendly AI bot created by [Your Name].", color=0x7289DA)
    embed.add_field(name="Author", value="Your Name")
    embed.add_field(name="Server Count", value=f"I am currently in {len(bot.guilds)} servers.")
    await ctx.send(embed=embed)

