import discord
from datetime import datetime

class Study_record(): 
    
    def __init__(self,name): #create a record of the user
        #user details
        self.name = name
        self.study_status = False
        #store time
        self.total_studytime = 0
        
    def user_register(self):
        return f"User {self.name} registered!"
    
    def user_start_study(self): #start a study session
        self.study_status = True
        self.session_start_time = datetime.now()
        self.day_when_study_start = datetime.today().day
        return f"User started studying at {self.session_start_time.hour} : {self.session_start_time.minute} : {self.session_start_time.second}"
    
    def user_end_study(self): #end a study session
        self.study_status = False
        self.session_end_time = datetime.now()
        self.total_studytime = self.total_studytime + (self.session_end_time - self.session_start_time).total_seconds()
        return f"User ended studying at {self.session_end_time.hour} : {self.session_end_time.minute} : {self.session_end_time.second}"
    
    def user_show_study(self): #show study details
        if self.study_status == True:
            time = (datetime.now() - self.session_start_time).total_seconds()
        else:
            time = self.total_studytime
    
        #self.total_studytime = self.total_studytime + (self.session_end_time - self.session_start_time).total_seconds()
        h = int( time// 3600)
        m = int(time // 60)
        s = int(time % 60)
        return f"You studied for {h} hours, {m} minutes and {s} seconds today!"
    
    def reset_time(self):
        self.total_studytime = 0

    def user_details(self):
        return f"User : {self.name}\nStudy status(true/false) : {self.study_status}\nTime studied : {self.total_studytime}"
    
    


class MyClient(discord.Client):     
    def __init__(self, *args, **kwargs):  
        super().__init__(*args, **kwargs)
        
        self.user_records = {} #dictionary for user and their records
        self.commands = {"show_commands" : "to see this dictioary",
                         "register_me" : "to register with the bot",
                         "start_study" : "to start a session",
                         "end_study" : "to end a study session",
                         "finished_study" : "indicates that u have finished today's study",
                         "show_study" : "shows u the time you have studied",
                         "check_user_details" : "to check the details of the user registered(for developer)"
                         }
        #self.leaderboard = []

    async def on_ready(self):
        print("---Bot ready!---")
    
    async def on_message(self,message): 
        if message.author == self.user:
            return
        else:
            if message.content == "show_commands":  # show commands
                bot_msg = ""
                for k,v in self.commands.items():
                    bot_msg = bot_msg + f"{k} - {v}\n"
                await message.channel.send(bot_msg)

            elif message.content == "register_me": # register command 
                if message.author in self.user_records.keys(): 
                    await message.channel.send(f"{message.author} is already registered!")
                else:
                    user_name = message.author
                    record = Study_record(user_name)

                    self.user_records[user_name] = record # bot creates a record for the user
                    await message.channel.send(self.user_records.get(user_name).user_register()) # send message that record created
                    
            elif message.content == "start_study": # session start command
                user_name = message.author
                await message.channel.send(self.user_records.get(user_name).user_start_study())

            elif message.content =="end_study": # session end command
                user_name = message.author
                await message.channel.send(self.user_records.get(user_name).user_end_study())

            elif message.content == "show_study": # show study details command
                user_name = message.author
                record = self.user_records.get(user_name)
                await message.channel.send(record.user_show_study())

            elif message.content == "finished_study":
                user_name = message.author
                record = self.user_records.get(user_name)
                bot_msg = self.user_records.get(user_name).user_show_study()
                await message.channel.send(bot_msg + "\nTime has been reset!")
            
            elif message.content == "check_user_details":
                user_name = message.author
                record = self.user_records.get(user_name)
                bot_msg = self.user_records.get(user_name).user_details()
                await message.channel.send(bot_msg)
            
            else:
                bot_msg = ""
                for k,v in self.commands.items():
                    bot_msg = bot_msg + f"{k} - {v}\n"
                await message.channel.send(f"Wrong command,choose one from the following\n" + bot_msg )
            


if __name__ == '__main__':
    #creates the bot
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = MyClient(intents = intents) #bot object created

    #unique token for the bot
    TOKEN = ""
    client.run(TOKEN)
