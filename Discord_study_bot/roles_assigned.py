import discord
from datetime import datetime

class Study_record():
    
    def __init__(self,name): # create a record of the user
        self.name = name 
        self.total_studytime = 0
        self.daily_studytime = 0
        self.weekly_studytime = 0
        self.monthly_studytime = 0

    
    def track_time(self): #track time spent studying
        if datetime.today().day == self.day_when_study_start:
            self.daily_studytime = self.total_studytime
        if datetime.today().day >= (self.day_when_study_start + 7):
            self.weekly_studytime = self.total_studytime
        if datetime.today().day >= (self.day_when_study_start + 30):
            self.monthly_studytime = self.total_studytime

        return
    
    def user_register(self):
        return f"User {self.name} registered!"
    
    def user_start_study(self): # start a study session
        self.session_start_time = datetime.now()
        self.day_when_study_start = datetime.today().day
        return f"User started studying at {self.session_start_time} on {datetime.today()}"
    
    def user_end_study(self): # end a study session
        self.session_end_time = datetime.now()
        self.total_studytime = self.total_studytime + (self.session_end_time - self.session_start_time).total_seconds()
        self.track_time()
        return f"User ended studying at {datetime.now()} on {datetime.today()}"
    
    def user_show_study(self): # show study details
        if datetime.today().day == self.day_when_study_start:
            return f"User studied for {int(self.total_studytime // 3600)} hours, {int(self.total_studytime // 60)} minutes and {int(self.total_studytime % 60)} seconds"
        if datetime.today().day >= (self.day_when_study_start + 7):
            return f"Hours studied by the user one week : {int(self.total_studytime//3600)}"
        if datetime.today().day >= (self.day_when_study_start + 30):
             return f"Hours studied by the user since one month : {int(self.total_studytime//3600)}"
    
    def check_roles(self):
        pass

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.user_records = {}
        self.commands = ["show_commands","register_me","start_study","end_study","show_study"]

    async def on_ready(self):
        print("---Bot ready!---")
    
    async def on_message(self,message):
        if message.author == self.user:
            return
        else:
            if message.content == "show_commands":  # show commands
                await message.channel.send(f"commands are : {self.commands}") 

            elif message.content == "register_me": # register command 
                if message.author in self.user_records.keys(): 
                    await message.channel.send(f"{message.author} is already registered!")
                else:
                    self.user_records[message.author] = Study_record(message.author) # bot creates a record for the user
                    await message.channel.send(self.user_records.get(message.author).user_register()) # send message that record created
                    
            elif message.content == "start_study": # session start command
                await message.channel.send(self.user_records.get(message.author).user_start_study())

            elif message.content =="end_study": # session end command
                await message.channel.send(self.user_records.get(message.author).user_end_study())

            elif message.content == "show_study": # show study details command
                await message.channel.send(self.user_records.get(message.author).user_show_study())

            else:
                await message.channel.send(f"Wrong command,choose one from the following : {self.commands}")
            


if __name__ == '__main__':

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = MyClient(intents = intents)

    TOKEN = "MTEwMjIwMzU2Mjg1NzA3NDgwOA.G4FS0N.ZRYZANSBLLgyIcJzKXzdqPeTCVcEw_7aLcbZ7w"
    client.run(TOKEN)
