import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[1].id)
engine.runAndWait()

def speak(text):
    engine.setProperty("voice", voices[0].id)
    engine.say(text)
    engine.runAndWait()

print("What is your name?")    
name = input()
speak("Hello, " + name + "I trust you are doing well.")
print("How do you feel?")
answer = input()
speak("I am here to ask you a very important question and if you pass you get the job, are you ready?")
print("are you ready?")
answer = input()
speak("Do you prefer ketchup or mustard?")
print("Do you prefer ketchup or mustard?")
answer = input()
if answer == "yes":
    speak("I want you back in my office by morning, we could use someone with your excellent taste among us.")
else:
    speak("Well its been fun, but we have more candidates to interview, I'm sure you can get hired elsewhere.")
