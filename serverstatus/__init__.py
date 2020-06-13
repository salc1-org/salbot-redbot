from .serverstatus import ServerStatus

def setup(bot):
    bot.add_cog(ServerStatus(bot))