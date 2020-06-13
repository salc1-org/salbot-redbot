from .userinfo import Userinfo
from .serverstatus import ServerStatus
from .maze import Maze

def setup(bot):
    #Userinfo
    bot.add_cog(Userinfo(bot))
    bot.add_cog(Maze(bot))
    #serverstatus
    channel_server_mapping = {
        588040378188431486: "2b2t.org",
        717524010249879592: "2b2t.org" #Testing discord channel
    }
    bot.add_cog(ServerStatus(bot, channel_server_mapping))