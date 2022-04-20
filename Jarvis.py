import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
from googlesearch import search as sch
from googlesearch import*
import webbrowser
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try: 
        with sr.Microphone() as source:
            print("Listening...")
            talk('Jarvis at your assistance')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', ' ')
                engine.runAndWait()
                print(command)
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', 'Playing'), command.replace('service', ' ')
        
        talk(song)
        print(song)
        pywhatkit.playonyt(song)
        
    
    elif 'search wikipedia for' in command:
        person = command.replace('search wikipedia for', '')
        talk('finding info on ' + person)
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    elif 'Whats the time' or 'Tell me the time' in command:
        if 'google' in command:
            topic = command.replace('google', '')
            talk('Please wait while I search for you')
            edge_path = r'C:\Windows\SystemApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe'
            for url in search(topic, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % topic)
            print(topic)
        else:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(time)
        
    
    elif 'google' in command:
        topic = command.replace('google', '')
        talk('Please wait while I search for you')
        edge_path = r'C:\Windows\SystemApps\Microsoft.MicrosoftEdge_8wekyb3d8bbwe'
        for url in search(topic, tld="co.in", num=1, stop = 1, pause = 2):
            webbrowser.open("https://google.com/search?q=%s" % topic)
        print(topic)

run_jarvis()