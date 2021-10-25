import time #Allows interaction witht the time object
import sys #Allows for interaction with the system object. 
from playsound import playsound #Will play the sound when the number reaches 0. install using pip install playsound in your command prompt on windows or pip3 install playsound on linux
#Download and place it into a folder for the script to use 

x = 10 #Define number to count down from 


while x < 20: #Will check if variable is less than 20
    print(x) #Will keep printing the contents of x while x is less than 
    x = x-1 #Will keep subtracting from the contents of x 
    time.sleep(1)#will pause the program to initiate the if statement. 
    if x == 0: #will initate an if condition if x is subtracted down to 0
        print("out of power, powering off")
        playsound("<Place the path to your audio file here>") #Place the directory of the audio file here. 
        sys.exit() #Ends the program to keep the console from showing any number less than 1. 
