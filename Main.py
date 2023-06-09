
import pyttsx3
import speech_recognition as sr
from Features import GoogleSearch



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',150)

def Speak(audio):
    print(voices)
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")
Speak("Hello sir, How are you")

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print(": Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f": Your Command : {query}\n")
    except:
        return ""
    return query.lower()

def TaskExe():
    while True:
        query = TakeCommand()
        if 'google search' in query:
            GoogleSearch(query)
        
        elif 'youtube search' in query:
            Query = query.replace("jarvis","")
            query = Query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)

        elif 'download' in query:
            from Features import DownloadYouTube
            DownloadYouTube()
            
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()
            
        elif 'ChromeSearch' in query:
            from Automations import ChromeSearch
            ChromeSearch(query)
            
        elif 'Youtube' in query:
            from Automations import YouTubeAuto
            YouTubeAuto()
            
        elif 'Window' in query:
            from Automations import Window
            Window()

        elif 'whatsapp message' in query:
            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("jarvis ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)

        elif 'my location' in query:
            from Features import My_Location
            My_Location()
            
        elif 'where is' in query:
            from Automations import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("jarvis" , "")
            GoogleMaps(Place)

        elif 'write a note' in query:
            from Automations import Notepad
            Notepad()

        elif 'dismiss' in query:
            from Automations import CloseNotepad
            CloseNotepad()

        elif 'time table' in query:
            from Automations import TimeTable
            TimeTable()

        elif 'activate the bulb' in query:
            from DataBase.HomeAuto.SmartBulb import Activate
            Activate()
            Speak("Should I Start Or Close The Bulb ?")
            step = TakeCommand()

            if 'close' in step:
                from DataBase.HomeAuto.SmartBulb import CloseLight
                CloseLight()

            elif 'start' in step:
                from DataBase.HomeAuto.SmartBulb import StartLight
                StartLight()
        else:
            from DataBase.ChatBot.ChatBot import ChatterBot
            reply = ChatterBot(query)
            Speak(reply)

            if 'bye' in query:
                break

            elif 'exit' in query:
                break

            elif 'go' in query:
                break
TaskExe()     

            
            



