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
import pyjokes

listener = sr.Recognizer()
jarvis = pyttsx3.init()
jarvis.setProperty("rate", 140)

# try and except statement to catch the error prevent the program from crashing
try:
    with sr.Microphone() as source:
        print("Jarvis is here. Call his attention.\n")

        # loop for user to say "hey, jarvis"
        while True:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'hey jarvis' in command:
                break

            else:
                jarvis.say("Say 'Hey Jarvis!' first.")
                jarvis.runAndWait()

        jarvis.say("Hi master. What's up?")
        jarvis.runAndWait()

        # loop for jarvis to listen to user again
        while True:

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if "repeat what i'm going to saying" in command or "please repeat me" in command:
                jarvis.say("Okay, master. I'm ready")
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
                jarvis.say("It's" + time + "master")
                jarvis.runAndWait()

            elif "date" in command:
                date = date.today().strftime("%B %d %Y")
                jarvis.say("Today is" + date + "master")
                jarvis.runAndWait()

            elif "who is" in command:
                person = command.replace('who is ', '')
                info = wikipedia.summary(person, 1)
                jarvis.say(info)
                jarvis.runAndWait()
            
            elif "joke" in command:
                jarvis.say(pyjokes.get_joke())
                jarvis.say("Hahaha. Master if you don't laugh at my joke I will get mad.")
                jarvis.runAndWait()

            elif "thank you" in command or "thanks" in command:
                jarvis.say("You are welcome master.")
                jarvis.runAndWait()

            elif "i love you" in command or "love you" in command:
                jarvis.say("I love you too master.")
                jarvis.runAndWait()

            elif "goodbye jarvis" in command or "goodbye" in command:
                jarvis.say("Thank you master. Goodbye!")
                jarvis.runAndWait()
                break

            else:
                jarvis.say("I don't know what you're saying, master. Please try again.")
                jarvis.runAndWait()

except:
    pass