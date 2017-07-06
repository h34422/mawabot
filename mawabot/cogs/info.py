#
# cogs/info.py
#
# mawabot - Maware's selfbot
# Copyright (c) 2017 Ma-wa-re, Ammon Smith
#
# mawabot is available free of charge under the terms of the MIT
# License. You are free to redistribute and/or modify it under those
# terms. It is distributed in the hopes that it will be useful, but
# WITHOUT ANY WARRANTY. See the LICENSE file for more details.
#

''' Has several commands that get guild information '''
import re
import unicodedata

import discord
from discord.ext import commands

__all__ = [
    'setup',
]

EMOJI_REGEX = re.compile(r'<:([A-Za-z~\-0-9]+):([0-9]+)>')

class Info:
    __slots__ = (
        'bot',
    )

    def __init__(self, bot):
        self.bot = bot

    # Commands
    @commands.command()
    async def emoji(self, ctx, *emojis: str):
        ''' Gets information about the given emoji(s) '''

        for emoji in emojis:
            match = EMOJI_REGEX.match(emoji)
            if match:
                await ctx.send(content=f'Emoji: `{match[1]}`\nID: `{match[2]}`')
            else:
                try:
                    name = unicodedata.name(emoji)
                    await ctx.send(content=f'Unicode name: `{name}`\nOrd: `{ord(name)}`')
                except:
                    self.bot.logger.warn(f'Not an emoji: {emoji}')

    @commands.command()
    async def uptime(self, ctx):
        ''' Gets the uptime of this self-bot '''

        await ctx.message.edit(content=self.bot.uptime)

def setup(bot):
    ''' Setup function to add cog to bot '''
    cog = Info(bot)
    bot.add_cog(cog)
