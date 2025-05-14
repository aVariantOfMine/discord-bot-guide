import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
@commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """Kick a user from the server."""
        await member.kick(reason=reason)
        await ctx.send(f"👢 Kicked {member.mention} for: {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="No reason provided"):
        """Ban a user from the server."""
        await member.ban(reason=reason)
        await ctx.send(f"🔨 Banned {member.mention} for: {reason}")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, user_name):
        """Unban a user using their name#tag."""
        banned_users = await ctx.guild.bans()
        name, discriminator = user_name.split("#")

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (name, discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"♻️ Unbanned {user.mention}")
                return
        await ctx.send("❌ User not found in bans.")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int = 5):
        """Clear recent messages."""
        await ctx.channel.purge(limit=amount + 1)  # +1 to remove the command too
        await ctx.send(f"🧹 Cleared {amount} messages!", delete_after=3)

async def setup(bot):
    await bot.add_cog(Moderation(bot))
