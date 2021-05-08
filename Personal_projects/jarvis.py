import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init()


def speak(text):
    print('[Jarvis] : ' + text)
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hours = int(datetime.datetime.now().hour)

    if 0 <= hours < 12:
        greeting = 'Good Morning! '

    elif 12 <= hours <= 16:
        greeting = 'Good Afternoon! '

    elif 16 < hours <= 24:
        greeting = 'Good Evening! '

    else:
        greeting = ''

    speak(f'{greeting}, I am Jarvis, How can i help you Sir!')


def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('% Listening %')
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("% Recognising %")
        query = r.recognize_google(audio, language='en-in')
        print('[You] : ' + query)

    except Exception as e:
        print(e)
        return 'None'

    return query


wish_me()
while True:
    query = take_command().lower()
    if 'thank you jarvis' in query or 'close jarvis' in query or 'jarvis close' in query:
        speak('Thank you sir, jarvis signing off')
        break
    query = query.replace('jarvis', '')

    if 'wikipedia' in query:
        query = query.replace('wikipedia', '')
        query = query.replace('search', '')
        query = query.replace('search wikipedia for', '')
        results = wikipedia.summary(query, sentences=1)
        speak('According to Wikipedia, ' + results)

    elif 'open youtube' in query:
        speak('Opening Youtube')
        webbrowser.open('https://youtube.com')

    elif 'open google' in query:
        speak('Opening Google')
        webbrowser.open('https://google.com')

    elif 'open stack overflow' in query:
        speak('Opening StackOverflow')
        webbrowser.open("https://stackoverflow.com")

    elif 'what' in query and 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, The time is {strTime}")
