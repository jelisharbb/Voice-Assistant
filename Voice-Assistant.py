# Say "Hey, Jarvis"
# Jarvis will listen, then you will talk
# Jarvis will respond
# reference: https://www.youtube.com/watch?v=AWvsXxDtEkU


# importing modules
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from datetime import date
import wikipedia

listener = sr.Recognizer()
jarvis = pyttsx3.init()
jarvis.setProperty("rate", 140)

# try and except statement to catch the error prevent the program from crashing
try:
    with sr.Microphone() as source:
        print("Jarvis is here. Call his attention.")

        # loop for user to say "hey, jarvis"
        while True:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'hey jarvis' == command:
                break

            else:
                print('Say "Hey, Jarvis" for him to listen.')

        jarvis.say("Hi, I'm listening")
        jarvis.runAndWait()

        # loop for jarvis to listen to user again
        while True:

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if "repeat what i'm saying" in command:
                jarvis.say("Okay, I'm ready")
                jarvis.runAndWait()

                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                jarvis.say(command)
                jarvis.runAndWait()
                print()

            elif "play" in command:
                song =  command.replace('play', '')
                jarvis.say("Playing" + song)
                jarvis.runAndWait()
                pywhatkit.playonyt(song)

            elif "time" in command:
                time = datetime.datetime.now().strftime("%I %M %p")
                jarvis.say("It's" + time)
                jarvis.runAndWait()

            elif "date" in command:
                date = date.today().strftime("%B %d %Y")
                jarvis.say("Today is" + date)
                jarvis.runAndWait()

            elif "who is" in command:
                person = command.replace('who is ', '')
                info = wikipedia.summary(person, 1)
                jarvis.say(info)
                jarvis.runAndWait()

            elif "goodbye jarvis" in command or "goodbye" in command:
                jarvis.say("Thank you. Goodbye!")
                jarvis.runAndWait()
                break

            else:
                jarvis.say("I don't know what you're saying. Try again.")
                jarvis.runAndWait()

except:
    pass