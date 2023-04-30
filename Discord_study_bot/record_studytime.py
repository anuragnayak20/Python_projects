import discord
from datetime import datetime

#creating bot client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

#recording the different users on the bot
student_list = []

#individual user record
class studytime_record:
    def __init__(self,author):
        self.student_id = author
        self.time_studied = 0
        self.start_time = datetime.now()

    def session_start(self):
        self.start_time = datetime.now()
        return "session started - study time recording"
    
    def session_end(self):
        self.time_studied = datetime.now() - self.start_time #timedelta object
        return "session ended - study time recorded"
        
    def display_studytime(self):
        time = self.time_studied.total_seconds()
        hour = time//3600
        minutes = time//60
        seconds = time % 60
        display_msg = f"{self.student_id} studied for {int(hour)} hours {int(minutes)} minutes {int(seconds)} seconds"
        return display_msg
        
#bot online
@client.event
async def on_ready():
    print("--- study bot online ---")

#reading the messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        if message.content == "register_me":
            student_list.append(studytime_record(message.author))
            await message.channel.send("user registered!")

        if message.content == "start_study":
            for student in student_list:
                if message.author == student.student_id:
                    txt_msg = student.session_start()
                    break
            await message.channel.send(txt_msg)

        if message.content == "end_study":
            for student in student_list:
                if message.author == student.student_id:
                    txt_msg = student.session_end()
                    break
            await message.channel.send(txt_msg)

        if message.content == "show_study":
            for student in student_list:
                if message.author == student.student_id:
                    txt_msg = student.display_studytime()
                    break
            await message.channel.send(txt_msg)

#token will remain private or locally stored.
token = "token_not_to_be_shared"
client.run(token)