
import pywhatkit
import wikipedia
from pywikihow import RandomHowTo, search_wikihow
import os
import speech_recognition as sr
import webbrowser as web
import bs4
import pyttsx3
from time import sleep
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

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

def GoogleSearch(term):
    query = term.replace("jarvis","")
    query = query.replace("what is","")
    query = query.replace("how to","")
    query = query.replace("what is","")
    query = query.replace("who is","")
    query = query.replace(" ","")
    query = query.replace("what do you mean by","")

    writeab = str(query)

    oooooo = open('C:\\Users\\Dell\\OneDrive\\Desktop\\Virtual assistant\\How To Make Jarvis\\Data.txt','a')
    oooooo.write(writeab)
    oooooo.close()

    Query = str(term)
    pywhatkit.search(Query)

    os.startfile('C:\\Users\\Dell\\OneDrive\\Desktop\\Virtual assistant\\How To Make Jarvis\\DataBase\\ExtraPro\\start.py')
    


    if 'how to' in Query:
        max_result = 1
        how_to_func = search_wikihow(query=Query,max_results=max_result)
        assert len(how_to_func) == 1
        how_to_func[0].print()
        Speak(how_to_func[0].summary)

    else:
        search = wikipedia.summary(Query,2)
        Speak(f": According To Your Search : {search}")
        


def YouTubeSearch(term):
    result = "https://www.youtube.com/results?search_query=" + term
    web.open(result)
    Speak("This Is What I Found For Your Search .")
    pywhatkit.playonyt(term)
    Speak("This May Also Help You Sir .")
    




def Alarm(query):

    TimeHere=  open('C:\\Users\\Dell\\Desktop\\Virtual assistant\\How To Make Jarvis\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("C:\\Users\\Dell\\Desktop\\Virtual assistant\\How To Make Jarvis\\DataBase\\ExtraPro\\Alarm.py")


def DownloadYouTube():
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=1840,y=28)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):


        url = YouTube(link)


        video = url.streams.first()


        video.download('C:\\Users\\Dell\\OneDrive\\Desktop\\Virtual assistant\\How To Make Jarvis\\DataBase\\Youtube\\')


    Download(Link)


    Speak("Done Sir , I Have Downloaded The Video .")

    Speak("You Can Go And Check It Out.")


    os.startfile('C:\\Users\\Dell\\OneDrive\\Desktop\\Virtual assistant\\How To Make Jarvis\\DataBase\\Youtube\\')

def SpeedTest():

    os.startfile("C:\\Users\\Dell\\OneDrive\\Desktop\\\Virtual assistant\\How To Make Jarvis\\DataBase\\Gui Programs\\SpeedTestGui.py")

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)

def My_Location():

    op = "https://www.google.com/maps/place/Kanpur,+Uttar+Pradesh/@26.4471501,80.255981,12z/data=!3m1!4b1!4m6!3m5!1s0x399c4770b127c46f:0x1778302a9fbe7b41!8m2!3d26.449923!4d80.3318736!16zL20vMDFfcTdo"
    Speak("Checking Your Location Sir Please Wait....")

    web.open(op)

    ip_add = requests.get('https://api.ipify.org').text

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'

    geo_q = requests.get(url)

    geo_d = geo_q.json()

    state = geo_d['city']

    country = geo_d['country']

    Speak(f"Sir , You Are Now In {state , country} .")


    
