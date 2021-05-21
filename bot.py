import os
from twitchio.ext import commands

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'], 
    client_id=os.environ['CLIENT_ID'], 
    nick=os.environ['BOT_NICK'], 
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.event
async def event_ready():
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws
    await ws.send_privmsg(os.environ['CHANNEL'],f"/me has arrived!")


@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return 

    await bot.handle_commands(ctx)

    if any(word in ctx.content.lower() for word in ["hello", "hi", "hey"]):
        await ctx.channel.send(f"Hey there, @{ctx.author.name}!")



@bot.command(name="lurk")
async def lurk(ctx):
    await ctx.send('Thanks for the lurk! Sit down, relax and have an AMAZING day!!')


@bot.command(name="socials")
async def socials(ctx):
    await ctx.send('Follow ProffesorLayto on Twitter: https://twitter.com/ProfessorLayto !')


@bot.command(name="so")
async def so(ctx):
    so_name = ctx.content.split(' ')[1]
    await ctx.send('HEY EVERYONE!! Go follow @' + so_name + '! They are pretty POG if ya ask me.....CHECK EM 
        OUT PLSSSSS!!!!')



if __name__ == "__main__":
    print("we good brodie")
    bot.run()
    

