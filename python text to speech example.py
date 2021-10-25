#These will import the necessary modules for this program to work
import pyttsx3
import speech_recognition as sr #These first two lines are used for text to speech 
import time #This module is used for the time object used in the function speak()

#use the command prompt to install pyttsx3 using the command pip install pyttsx3 


engine = pyttsx3.init() 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.runAndWait()

def speak():
    engine.say("Processing")
    engine.say("Python is a useful programming language that is popular for  software development.")
    engine.say("It is ideal for beginners because it is powerful and very easy to learn in that  it is close to english and has a simple syntax.")
    engine.runAndWait()


speak()


