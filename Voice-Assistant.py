# Say "Hey, Jarvis"
# Jarvis will listen, then you will talk
# Jarvis will respond
# reference: https://www.youtube.com/watch?v=AWvsXxDtEkU


# importing modules
import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
jarvis = pyttsx3.init()
jarvis.setProperty("rate", 140)

# try and except statement to catch the error prevent the program from crashing
try:
    with sr.Microphone() as source:
        print()
        print("Jarvis is here. Call his attention.")

        while True:
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'hey jarvis' == command:
                break

            else:
                print('Say "Hey, Jarvis" for him to listen.')

        # print()
        # print("Hi! I'm listening...")
        jarvis.say("Hi, I'm listening")
        jarvis.runAndWait()

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
                continue

            elif "goodbye jarvis" or "goodbye" in command:
                jarvis.say("Thank you. Goodbye!")
                jarvis.runAndWait()
                break

except:
    pass