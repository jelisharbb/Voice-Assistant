# Say "Hey, Jarvis"
# Jarvis will listen, then you will talk
# Jarvis will respond
# reference: https://www.youtube.com/watch?v=AWvsXxDtEkU


# importing modules
import speech_recognition as sr

listener = sr.Recognizer()

# try and except statement to catch the error prevent the program from crashing
try:
    with sr.Microphone() as source:
        # print()
        # print("Hi! I'm listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)

        while True:
            command = command.lower()
            if 'hey jarvis' == command:
                break

            else:
                print('Say "Hey, Jarvis" first.')

        print()
        print("Hi! I'm listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        print(f"You: {command.capitalize()}.")
        print()

except:
    pass
