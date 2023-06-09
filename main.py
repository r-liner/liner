import nextcord
from nextcord.ext import commands


intents = nextcord.Intents.all()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} (ID: {bot.user.id})")


@bot.event
async def on_message(message: nextcord.Message):
    print(f"Received message: {message.content}")
    await bot.process_commands(message)


@bot.command()
async def dm(ctx, user: nextcord.User, *, message: str):
    print(f"Sending DM to user {user.name} ({user.id}): {message}")
    await user.send(message)


@bot.command()
async def dm_role_members(ctx, role: nextcord.Role, *, message: str):
    print(f"Sending DM to members of role {role.name} ({role.id}): {message}")
    for member in role.members:
        await member.send(message)


@bot.command()
async def start_saper(ctx):
    print(f"Starting new game of saper.")
 
@bot.command()
async def saper(ctx, row: int, col: int):
    print(f"Choosing cell ({row}, {col}) in saper game.")

bot.run("")