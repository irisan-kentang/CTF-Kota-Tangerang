#!/usr/bin/env python3
from discord.ext.commands import MemberConverter
from discord.ext import commands,tasks

from difflib import get_close_matches
from datetime import datetime

import os
import discord
import asyncio
import typing
import subprocess

bot = commands.Bot(command_prefix=commands.when_mentioned_or("?"),description="",intents=discord.Intents.all(),activity=discord.Game(name=""))

class MyHelp(commands.HelpCommand):
    def get_command_signature(self, command):
        return  f'{self.clean_prefix}{command.qualified_name} {command.signature}'

    async def send_bot_help(self, mapping):
        channel = self.get_destination()
        embed = discord.Embed(title="Wishing well is here ! 🎺",color=0x03fcc6,timestamp=datetime.utcnow(),description="Just give me a thing, then I'll grant your wish.")
        for cog, commands in mapping.items():
            filtered = await self.filter_commands(commands, sort=True)
            command_signatures = [self.get_command_signature(c) for c in filtered]
            if command_signatures:
                cog_name = getattr(cog, "qualified_name", "No Category")
                embed.add_field(name=cog_name, value="\n".join(command_signatures), inline=False)
        await channel.send(embed=embed)
    

class Commands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_guild_join(self,guild:discord.Guild):
        """Create the role muted as soon as the bot joins the guild, if no muted role exists. Disable send messages permissions and speak permissions for muted role in every channel"""
        for role in guild.roles:
            if role.name.lower() == "muted":
                return
        mutedRole = await guild.create_role(name="Muted",permissions=discord.Permissions(send_messages=False,speak=False))
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, send_messages = False, speak = False)
        

    @commands.command(aliases=["giveme"],help="Give me something worth")
    @commands.has_permissions(send_messages=True)
    async def givemea(self,ctx,value):
        if value == 's3cret_fl4g_db02e5e':
            content = os.getenv('FLAG')
            embedVar = discord.Embed(description=f"Thanks, I feel better now. Here's my gift\n\n **{content}**",color=0xffffff)
            await ctx.send(embed=embedVar)
        else:
            embedVar = discord.Embed(description=f"Sorry. You need to give me something better",color=0xaaffaa)
            await ctx.send(embed=embedVar)

    @commands.command(help="About me")
    @commands.has_permissions(send_messages=True)
    async def aboutme(self,ctx):
        embedVar = discord.Embed(description=f"Made with :heart:\n\n Deployed using Docker by ||k3gabut4ndev||",color=0x1685b5)
        await ctx.send(embed=embedVar)



class ErrorHandler(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandNotFound):
            cmd = ctx.invoked_with
            cmds = [cmd.name for cmd in bot.commands]
            matches = "\n".join(get_close_matches(cmd, cmds,n=3))
            if len(matches) > 0:
                await ctx.send(f"Command \"{cmd}\" not found. Maybe you meant :\n{matches}")
            else:
                await ctx.send(f'Command "{cmd}" not found, use the help command to know what commands are available')
        elif isinstance(error,commands.MissingPermissions):
            await ctx.send(error)
        elif isinstance(error,commands.MissingRequiredArgument):
            await ctx.send(error)
        elif isinstance(error,commands.NotOwner):
            return await ctx.send("You must be owner of this bot to perform this command.")


@bot.event
async def on_ready():
    print(f'Logged as {bot.user.name}')

TOKEN = os.getenv('TOKEN')

bot.help_command= MyHelp()
bot.add_cog(Commands(bot))
bot.add_cog(ErrorHandler(bot))
bot.run(TOKEN)
