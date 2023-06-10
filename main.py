import nextcord
from nextcord.ext import commands
import configparser
import os

config = configparser.ConfigParser()
config.read("config.ini")

intents = nextcord.Intents.all()

owners = [1076076913359077407]

client = commands.Bot(command_prefix=config["bot"]["prefix"], intents=intents, owner_ids=owners)


@client.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        client.load_extension(f"cogs.{extension}")
        print(f"Cog {extension} is loaded.")
        await ctx.send(f"Cog **{str.upper(extension)}** is loaded.")

    except Exception as error:
        print(error)
        await ctx.send("Неверное имя или невозможно загрузить")


@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        client.unload_extension(f"cogs.{extension}")
        print(f"Cog {str.upper(extension)} is unloaded.")
        await ctx.send(f"Cog **{str.upper(extension)}** is unloaded.")

    except Exception as error:
        print(error)
        await ctx.send("Неверное имя или невозможно загрузить")


@client.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")
        print(f"Cog {str.upper(extension)} is reloaded.")
        await ctx.send(f"Cog **{str.upper(extension)}** is reloaded.")

    except Exception as error:
        print(error)
        await ctx.send("Неверное имя или невозможно загрузить")


for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


try:
    client.run(config["bot"]["token"])

except Exception as err:
    print(err)

except nextcord.PrivilegedIntentsRequired:
    exit("Login failure! Privileged Intents not enabled.")

except nextcord.errors.LoginFailure:
    exit("Login failure! Token is required.")
