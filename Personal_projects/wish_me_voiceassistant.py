import pyttsx3
import datetime

engine = pyttsx3.init()

def speak(text):
    print("[Jarvis] :" + text)
    engine.speak(text)
    engine.runAndWait()

def wish_me():
    hours = int(datetime.datetime.now()).hour

    if 0 <= hours <= 12:
        greeting = 'Good Morning'

    elif 12 < hours <= 16:
        greeting = 'Good Afternoon'

    elif 16 < hours <= 24:
        greeting = 'Good Evening'

    else:
        greeting = ''

    print(greeting + 'How can i help you Sir!')

wish_me()

