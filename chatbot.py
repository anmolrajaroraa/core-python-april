import random
import os
import subprocess
from datetime import datetime
import webbrowser

greetIntent = ["I am fine. What about you", "I am doing great",
               "I am fine", "Everything is good. What's up with you"]
musicIntent = ["play a song for me", "play something for me",
               "play some bollywood song", "play some song from my library"]
dateIntent = ["date please", "what's the date today", "tell me today's date"]
timeIntent = ["time please", "what's the time right now", "tell me the time"]
greetTemplates = ["I am also doing great.", "I am just a humanoid.",
                  "I am feeling quite busy. People make me work a lot.", "I am also good. Is there any task for me?"]

while True:
    message = input("Enter your message: ")

    if message == "hi" or message == "hello" or message == "namaste" or message == "hola":
        print("hi, there. how you doin' ?")

    elif message in greetIntent:
        print(random.choice(greetTemplates))

    elif message.startswith('open'):
        # open google
        websiteName = message.partition(' ')[-1]
        webbrowser.open(f"https://{websiteName}.com")

    elif message.startswith('run'):
        # run google chrome
        # appName = message.partition(' ')[-1]
        # subprocess.call(['open', f'/Applications/{appName}.app'])
        appPath = input("Enter the complete path for the application")
        os.startfile("cmd")

    elif message in musicIntent:
        # os.startfile()
        # change location for searching songs
        os.chdir(
            "/Users/anmolrajarora/Documents/adv-python-reg-dec/MusicPlayer/songs")
        # print(os.getcwd())  # get current working directory
        # print(os.listdir())  # get all the files from cwd
        # os.chdir("C:/users/username/Documents/songs")
        # os.chdir("C:\\users\\username\\Documents\\songs")
        songs = os.listdir()
        print('''
            1. Play a random song
            2. Choose a song
        ''')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            song = random.choice(songs)
        else:
            for i, song in enumerate(songs):
                print(f"{i+1}. {song}")
            choice = int(input("Which song do you want to play : "))
            song = songs[choice - 1]
        # os.startfile(song)
        subprocess.call(["open", song])

    elif message in dateIntent:
        now = datetime.now()
        print(now.strftime("%d/%m/%y"))

    elif message in timeIntent:
        now = datetime.now()
        print(now.strftime("%H:%M:%S %p"))

    elif message == "bye" or message == "goodbye" or message == "see you later":
        print("bye, see you soon..")
        break

    else:
        print("I don't understand")

# songName = "Chal Ghar Chalein"
# # src = f"https://cdn10.upload.solutions/5f2c7d80125618dead7e2c1d04596549/phsov/{songNameSplitted[0]}%20{songNameSplitted[1]}%20{songNameSplitted[2]}-(Mr-Jatt.com).mp3"

# src = f"https://cdn10.upload.solutions/5f2c7d80125618dead7e2c1d04596549/phsov/{songName}-(Mr-Jatt.com).mp3"
# src = src.replace(" ", "%20")
# print(src)


# from datetime import datetime
# >>> datetime.now()
# datetime.datetime(2020, 5, 21, 12, 32, 45, 253329)
# >>> now = datetime.now()
# >>> type(now)
# <class 'datetime.datetime'>
# >>> now.strftime('A')
# 'A'
# >>> now.strftime('%A')
# 'Thursday'
# >>> now.strftime('%a')
# 'Thu'
# >>> now.strftime('%B')
# 'May'
# >>> now.strftime('%b')
# 'May'
# >>> now.strftime('%C')
# '20'
# >>> now.strftime('%Y')
# '2020'
# >>> now.strftime('%y')
# '20'
# >>> now.strftime('%D')
# '05/21/20'
# >>> now.strftime('%d')
# '21'
# >>> now.strftime('%m')
# '05'
# >>> now.strftime('%d/%m/%y')
# '21/05/20'
# >>> now.strftime('%H')
# '12'
# >>> now.strftime('%M')
# '33'
# >>> now.strftime('%S')
# '02'
# >>> now.strftime('%s')
# '1590044582'
# >>> now.strftime('%p')
# 'PM'
