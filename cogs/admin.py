import nextcord
from nextcord.ext import commands


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["dm"])
    @commands.is_owner()
    async def direct_message(self, ctx, user: nextcord.User, *, message: str):
        try:
            await user.send(message)
            await ctx.send("Сообщение отправлено")

        except nextcord.Forbidden:
            await ctx.send("У пользователя заблокированы ЛС. Или этот пользователь - бот.")

    @commands.command(aliases=["rdm"])
    @commands.is_owner()
    async def role_direct_message(self, ctx, role: nextcord.Role, *, message: str):
        members = role.members
        for member in members:
            try:
                await member.send(message)
                await ctx.send(f'Сообщение отправлено **{member.name}**')
            except nextcord.HTTPException:
                await ctx.send(f'Не удалось отправить сообщение пользователю **{member.name}**')
                
    @commands.command()
    async def give_access(self, ctx, user_name: str, channel_name: str):
        member = ctx.guild.get_member_named(user_name)
        channel = nextcord.utils.get(ctx.guild.channels, name=channel_name)
        await channel.set_permissions(member, read_messages=True)

    @commands.command()
    async def remove_access(self, ctx, user_name: str, channel_name: str):
        member = ctx.guild.get_member_named(user_name)
        channel = nextcord.utils.get(ctx.guild.channels, name=channel_name)
        await channel.set_permissions(member, overwrite=None)


def setup(client):
    client.add_cog(Admin(client))
