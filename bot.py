import os
import asyncio
from twitchio.ext import commands
import random

bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'], 
    client_id=os.environ['CLIENT_ID'], 
    nick=os.environ['BOT_NICK'], 
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

#Variables for some of the commands 

nouns = ("Actor", "Gold" , "Painting", "Advertisement", "Grass", "Parrot", "Afternoon", "Greece",  "Pencil", "Airport" ,"Guitar" ,"Piano", "Ambulance", "Hair", "Pillow",
            "Animal", 	"Hamburger", 	"Pizza Answer", "Helicopter", "Planet Apple",	"Helmet", 	"Plastic", "Army", "Holiday",	"Honey", "Potato", "Balloon", "Horse", "Queen",
        "Banana", "Hospital", "Quill", "Battery", "House" , "Rain", "Beach", "Hydrogen", "Rainbow", "Beard" , "Ice" , "Raincoat", "Bed", "Insect", 	"Refrigerator",
        "Restaurant", "Boy", "Iron", "River", "Branch", "Island", "Rocket", "Breakfast" , "Room", "Brother", "Jelly" , "Rose")

verbs = ("Accept", "Guess", "Achieve", 	"Harass", "Add", "Hate", "Admire", 	"Hear", "Admit" ,"Help","Adopt", "Hit","Advise", "Hope","Agree", "Identify",
        "Allow", 	"Interrupt", "Announce", "Introduce","Appreciate", 	"Irritate","Approve", 	"Jump","Argue", 	"Keep","Arrive", 	"Kick",
        "Ask", 	"Kiss","Assist", "Laugh","Attack", 	"Learn","Bake", "Leave","Bathe", "Lend","Be", "Lie","Beat", "Like","Become", "Listen",
        "Beg", 	"Lose","Behave", 	"Love","Bet", 	"Make", "Boast", "Marry","Boil", "Measure","Borrow", "Meet","Breathe", 	"Move","Bring", "Murder",
        "Build", "Obey","Burn", "Offend")

adv = ( "almost", "deeply", "enough", "hardly", "fairly", "fully", "least", "most", "just", "nearly", "quite", "again", "usually", "sometimes", "often", "easily", 
        "fondly", "gently", "mysteriously", "safely", "quietly", "well", "above", "into", "out", "upward", "now", "yet", "only", "daily", "later", "sometime")

adj = ( "adorable","beautiful", "clean", "drab", "elegant", "fancy", "glamorous", "handsome", "long", "magnificent", "old-fashioned", "plain", "quaint", 
        "sparkling", "ugliest", "unsightly", "wide-eyed", "red", "orange","yellow","green","blue","purple","gray","black","white", "alive","better","careful",
        "clever","dead","easy","famous","gifted","helpful", "ancient", "brief", "late", "early", "cooing", "loud", "big", "little", "raspy", "breeze", "boiling", 
        "damp", "dry", "few", "full", "substantial")

card_name = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Ace", "Jack", "Queen", "King")

card_type = ("Clubs", "Diamonds", "Hearts", "Spades")

text_emotes = ("( ͡° ͜ʖ ͡°)", "¯\_(ツ)_/¯", "( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)", "(▀̿Ĺ̯▀̿ ̿)", "༼ つ ◕_◕ ༽つ", "(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ✧ﾟ･: *ヽ(◕ヮ◕ヽ)", "ರ_ರ", "(▰˘◡˘▰)", "(´・ω・)っ由", "☜(⌒▽⌒)☞", 
                "｡◕‿‿◕｡", "(ง°ل͜°)ง", "(~˘▾˘)~", "(づ￣ ³￣)づ", "(ᵔᴥᵔ)", "| (• ◡•)| (❍ᴥ❍ʋ)", "[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]", "[̲̅$̲̅(̲̅5̲̅)̲̅$̲̅]", "ʕ•ᴥ•ʔ", "☼.☼", "≧☉_☉≦", "(>ლ)")

bot_phrase = ("Doing great!" , "Couldn't be better!", "FANTASTIC!", "Supercalifragilisticexpialidocious.", "We be good!", "Amazing!", "Living my best life!", "Coolio dude.")


#runs when the bot has connected to the chat
@bot.event
async def event_ready():
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws
    await ws.send_privmsg(os.environ['CHANNEL'],f"/me has arrived!")
    

    
#how the bot responds to other messages besides its own 
@bot.event
async def event_message(ctx):
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return 

    await bot.handle_commands(ctx)

    if any(word in ctx.content.lower() for word in ["cool", "nice", "sweet", "sick"]):
        await ctx.channel.send(f"I agree! @{ctx.author.name}!")
    
    elif 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Hi there, @{ctx.author.name}! How are you on this fine day?")

    elif '@prof_apprentice' in ctx.content.lower():
        await ctx.channel.send(f"What is it you need, @{ctx.author.name}?")

    elif 'how are you' in ctx.content.lower():
        phrases = [bot_phrase]
        await ctx.channel.send(" ".join([random.choice(i) for i in phrases]) + " Thanks for asking!")

    elif 'thanks' in ctx.content.lower():
        await ctx.channel.send(f"You're very welcome, @{ctx.author.name}!")




@bot.command(name = "welcome")
async def welcome_message(ctx):
    name = ctx.content.split(' ')[1]
    await ctx.send("Welcome to the stream " + name + ", thanks for popping in! Grab a seat, relax and have fun!")


#lurk command if lurking the stream 
@bot.command(name="lurk")
async def lurk(ctx):
    await ctx.send(f"Thanks for the lurk @{ctx.author.name}! You are POG! Sit down, relax and have an AMAZING day!!")


#social command that provides links to my current social medias
#after the initial command, the message will repeat every 30 minutes 
@bot.command(name="socials")
async def socials(ctx):
    #await ctx.send('Follow ProfessorLayto on Twitter: https://twitter.com/ProfessorLayto and Instagram: https://www.instagram.com/qu1616/ !')
    chan = bot.get_channel("professorlayto")
    loop = asyncio.get_event_loop()
    while True:
        await loop.create_task(chan.send("Be sure to follow ProfessorLayto on twitter! https://twitter.com/ProfessorLayto" ))
        await asyncio.sleep(1800)


#shout out command to give other streamers in chat a shout out 
@bot.command(name="so")
async def so(ctx):
    so_name = ctx.content.split(' ')[1]
    await ctx.send('HEY EVERYONE!! Go follow ' + so_name + '! They are pretty POG if ya ask me.....CHECK EM OUT PLSSSSS!!!!')


#donate command that provides the link to donations 
@bot.command(name="donate")
async def donate(ctx):
    await ctx.send('Donate to ProfessorLayto here: https://streamlabs.com/professorlayto/tip ! All donations go twoards the channel! Thank you so much!!!!')


#phrase command, creates a random phrase with a noun, verb, adverb and adjective.
@bot.command(name="phrase")
async def phrase(ctx):
    words = [nouns, verbs, adv, adj]
    await ctx.send('Your phrase is: ' + '"'+ " ".join([random.choice(i) for i in words]) +'!"')


#draw command, allows a user to draw a random card from a 52 card set 
@bot.command(name="draw")
async def draw(ctx):
    names = [card_name]
    types = [card_type]
    await ctx.send("You drew the " + " ".join([random.choice(i) for i in names]) + " of " + " ".join([random.choice(i) for i in types]) + f"! Nice pick @{ctx.author.name}!")


#text emote commands, randomly generates a text emote 
@bot.command(name="temote")
async def temote(ctx): 
    emote = [text_emotes]
    await ctx.send(" ".join([random.choice(i) for i in emote]))



#the main function 
if __name__ == "__main__":
    print("we good brodie")
    bot.run()
    

