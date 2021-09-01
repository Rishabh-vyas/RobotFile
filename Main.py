import speech_recognition as sr
from gtts import gTTS
import playsound
import pyttsx3
import os
import weathercom
import json
import datetime
import pywhatkit
import wikipedia

r = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


talk('Hello, i am Assistance of SKITM ')

def voice_command_processor(ask=False):
    with sr.Microphone() as source:
        if(ask):
            talk(ask)
        audio = r.listen(source,phrase_time_limit=4)

        text = ''
        try:
            text=r.recognize_google(audio)
            # talk(text)
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError as e:
            print("service is down")

        return text.lower()



def audio_playback(text):
    filename = "test.mp3"
    tts = gTTS(text=text, lang='en-us')
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


def execute_voice_command(text):
    if "who are you" in text:
        talk("i am a i voice assistance system")

    if "weather" in text:
        city = voice_command_processor("which city")
        humidity, temp, phrase = weatherReport(city)
        talk("currently in " + city + "  temperature is " + str(temp)
                       + " degree celsius, " + "humidity is " + str(humidity) + " percent and sky is " + phrase)
        print("currently in " + city + "  temperature is " + str(temp)
              + "degree celsius, " + "humidity is " + str(humidity) + " percent and sky is " + phrase)

    if 'time' in text:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    if 'define' in text in text:
        info = text.replace('define', '')
        data = wikipedia.summary(info, 2)
        talk(data)

    if 'play' in text:
        song = text.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    if 'search' in text:
        query = text.replace('search', '')
        talk('Searching' + query)
        pywhatkit.search(query)

    if 'create' in text or 'develop' in text:
        talk('PR Team.')

    if 'shivaji rao college' in text or 'engineering college' in text or 'collage' in text:
        talk('Shivaji Rao Kadam Institute of Technology & Management, is a college in Indore, India run by the Transnational Knowledge Society. It was formerly known as Acropolis Technical Campus')

    if 'hod' in text or 'head of department' in text:
        talk('Professor Prashant Sir')

    if 'dbms' in text or 'faculty' in text:
        talk('Professor Brajesh Sir')

    if 'how are you' in text or 'you are good' in text:
        talk('i am fine thankyou')

    if 'branch' in text or 'streams' in text:
        talk('there are Computer Science, Mechanical , Civil, Electronics ')

    if 'college event' in text or 'college event' in text:
        talk('there is lots of events in our college like isohack , technical webinar , aarambh , joy of giving Etcetera')

    if 'team members' in text or 'team person' in text:
        talk('Rishabh vyas ,Rishabh soni, Rahul Upadhyay , Pratham Bhawsar ,Rishi soni')

    if 'slow motion song' in text or 'motion song' in text:
        talk('Aaja    ,   doob    ,   jaaun    ,    teri    ,    aankhon    ,    ke    ,    ocean    ,    mein    ,    Slow    ,    motion    ,    mein    ,    Aaja    ,    doob    ,    jaaun    ,    teri    ,    aankhon    ,    ke    ,    ocean    ,   mein    ,    Slow    ,    motion    ,    mein')

    if 'pal do pal song' in text or 'shayar song ' in text:
        talk('main,pal,do,pal,kaa,shaayar,huun,pal,humain,pal,do,pal,kaa,shaayar,huun,pal,hu ')


    if 'placement' in text or 'hirirng' in text:
        talk(' We have already partnered with over 100 companies across various sectors, with brands like IBM, Capgemini, TCS, Digivalet, Accenture, BYJU’s and many more, with potential packages ranging from 4-10 lacs. We also work extensively on developing the overall personality and communication skills of our students to better prepare them for the job market.')


def weatherReport(city):
    weatherDetails = weathercom.getCityWeatherDetails(city)
    humidity = json.loads(weatherDetails)["vt1observation"]["humidity"]
    temp = json.loads(weatherDetails)["vt1observation"]["temperature"]
    phrase = json.loads(weatherDetails)["vt1observation"]["phrase"]
    return humidity, temp, phrase


while True:
    command = voice_command_processor()
    print(command)
    execute_voice_command(command)
