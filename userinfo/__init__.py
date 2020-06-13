from .userinfo import Userinfo

def setup(bot):
    bot.add_cog(Userinfo(bot))