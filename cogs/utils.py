import discord
from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Replies with bot latency."""
        latency = round(self.bot.latency * 1000)  # Convert to ms
        await ctx.send(f"Pong! 🏓 Latency is {latency}ms")

    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(title="Server Info", color=discord.Color.green())
        embed.add_field(name="Name", value=guild.name, inline=False)
        embed.add_field(name="Owner", value=guild.owner, inline=False)
        embed.add_field(name="Members", value=guild.member_count, inline=False)
        
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        await ctx.send(embed=embed)


    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        """Shows info about a user."""
        member = member or ctx.author  # Default to the person who used the command
        embed = discord.Embed(title="User Info", color=discord.Color.blue())
        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name="Username", value=member, inline=True)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.add_field(name="Joined", value=member.joined_at.strftime("%b %d, %Y"), inline=False)
        embed.add_field(name="Top Role", value=member.top_role, inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Utils(bot))
