#modules needed

from gtts import gTTS
import speech_recognition as sr
import pyttsx3
import time
from bs4 import BeautifulSoup
import requests
import random

#welcome
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)
engine.say('Hello Boss!')
engine.runAndWait()

#funcitons

def Speak(audio):
    "speaks audio passed as argument"
    print(audio)
    for line in audio.splitlines():
        engine.say(audio)
        engine.runAndWait()


def Joke():
        import requests
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            print(str(res.json()['joke']))
            Speak(str(res.json()['joke']))
        else:
            Speak('oops!I ran out of jokes')
            print('oops!I ran out of jokes')


def myCommand():
    "listens for commands"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('I am Ready...')
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):
    "if statements for executing commands"
    if 'time' in command:
        Speak(time.asctime())

    elif 'open reddit' in command:
        reg_ex = re.search('open reddit (.*)', command)
        url = 'https://www.reddit.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
        exit()  #exit loop        

    elif 'what\'s up' in command:
        Speak('Just doing my thing')
    
    elif 'thank you' in command:
        Speak('Glad to be of service.')
        print('Glad to be of service.')
        exit() #exit loop
    elif 'joke' in command:
        Joke()



Speak('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())
