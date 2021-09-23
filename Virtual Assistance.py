import pyttsx3
import speech_recognition as sr
import pyaudio
import webbrowser  
import datetime  
import wikipedia
import os
  
  

def takeCommand():
  
    r = sr.Recognizer()
  
    # from the speech_Recognition module 
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        print('Listening')
          
        # seconds of non-speaking audio before 
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
          
        # Now we will be using the try and catch
        # method so that if sound is recognized 
        # it is good else we will have exception 
        # handling
        try:
            print("Recognizing")
              
            # for Listening the command in indian
            # english we can also use 'hi-In' 
            # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("the command is printed=", Query)
              
        except Exception as e:
            print(e)
            print("Say that again maalik")
            return "None"
          
        return Query
  
def speak(audio):
      
    engine = pyttsx3.init()
    
    voices = engine.getProperty('voices')
      
    # setter method .[0]=male voice and 
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[1].id)
      
    # Method for the speaking of the the assistant
    engine.say(audio)  
      
    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()
  
def tellDay():
      
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
  
  
def tellTime():
      
    # This method will give the time
    time = str(datetime.datetime.now())
      

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak(self, "The time is " + hour + "Hours and" + min + "Minutes maalik")    
  
def Hello():
      
    #  when the assistant is called it will say hello and then 
    speak("hello malik I am your VA assistant \n Tell me how may I help you")



def openApp():
  

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
  
# changing index changes voices but ony
# 0 and 1 are working here
    engine.setProperty('voice', voices[1].id)
    engine.runAndWait()
    print("")
    print("")
  
# introduction
    print(" You are one step far...")
    engine.say(' can you repeate which application you want to open')
  
    print("")
    pyttsx3.speak("Welcome to my tools")
    print("")
    print("")
  
    pyttsx3.speak("Speak which app you want to open")
  
    while True:
        # take input
        print("    Speak which app you want to open : ", end='')
        

        p = takeCommand()
        p = p.upper()
        print(p)
  
        if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
            pyttsx3.speak("Type Again")
            print(".")
            print(".")
            continue
  
        # assignements for diffenet applications in the menu
        elif ("GOOGLE" in p) or ("SEARCH" in p) or ("WEB BROWSER" in p) or ("CHROME" in p) or ("BROWSER" in p) or ("4" in p):
            pyttsx3.speak("Opening")
            pyttsx3.speak("GOOGLE CHROME")
            print(".")
            print(".")
            os.system("chrome")
  
        elif ("IE" in p) or ("MSEDGE" in p) or ("EDGE" in p) or ("8" in p):
            pyttsx3.speak("Opening")
            pyttsx3.speak("MICROSOFT EDGE")
            print(".")
            print(".")
            os.system("msedge")
  
        elif ("NOTE" in p) or ("NOTES" in p) or ("NOTEPAD" in p) or ("EDITOR" in p) or ("9" in p):
            pyttsx3.speak("Opening")
            pyttsx3.speak("NOTEPAD")
            print(".")
            print(".")
            os.system("Notepad")
  
        elif ("VLCPLAYER" in p) or ("PLAYER" in p) or ("VIDEO PLAYER" in p) or ("5" in p):
            pyttsx3.speak("Opening")
            pyttsx3.speak("VLC PLAYER")
            print(".")
            print(".")
            os.system("VLC")
  
        elif ("VICE CITY" in p) or ("GTA" in p) or ("6" in p):
            pyttsx3.speak("Opening")
            pyttsx3.speak("GTA VICE CITY")
            print(".")
            print(".")
            os.system("GTA VICE CITY")
  
        elif ("PHOTOSHOP" in p) or ("PS" in p) or ("PHOTOSHOP CC" in p) or ("7" in p):
            pyttsx3.speak("Opening")
            pyttsx3.speak("ADOBE PHOTOSHOP")
            print(".")
            print(".")
            os.system("photoshop")
  
        elif ("TELEGRAM" in p) or ("TG" in p) or ("10" in p):
            pyttsx3.speak("Opening")
            pyttsx3.speak("TELEGRAM")
            print(".")
            print(".")
            os.system("telegram")
  
        elif ("EXCEL" in p) or ("MSEXCEL" in p) or ("SHEET" in p) or ("WINEXCEL" in p) or ("3" in p):
            pyttsx3.speak("Opening")
            pyttsx3.speak("MICROSOFT EXCEL")
            print(".")
            print(".")
            os.system("excel")
  
        elif ("SLIDE" in p) or ("MSPOWERPOINT" in p) or ("PPT" in p) or ("POWERPNT" in p) or ("2" in p):
            pyttsx3.speak("Opening")
            pyttsx3.speak("MICROSOFT POWERPOINT")
            print(".")
            print(".")
            os.system("powerpnt")
  
        elif ("WORD" in p) or ("MSWORD" in p) or ("1" in p):
            pyttsx3.speak("Opening")
            pyttsx3.speak("MICROSOFT WORD")
            print(".")
            print(".")
            os.system("winword")
  
        # close the program
        elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
            pyttsx3.speak("Exiting")
            break
  
        # ivalid input
        else:
            pyttsx3.speak(p)
            print("Is Invalid,Please Try Again")
            pyttsx3.speak("is Invalid,Please try again")
            print(".")
            print(".")






  
def Take_query():
  
    # calling the Hello 
    Hello()
      
    # This loop is infinite as it will take and end on bye

    while(True):
          
 
        # output
        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening Youtube ")
              
            
            webbrowser.open("www.youtube.com")
            continue
          
        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            continue
              
        elif "which day it is" in query:
            tellDay()
            continue
          
        elif "tell me the time" in query:
            tellTime()
            continue
          
        # this will exit and terminate the program
        elif "bye" in query:
            speak("Bye. Check Out GFG for more exicting things")
            exit()
          
        elif "from wikipedia" in query:
              
            # a information from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
              
           
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
          
        elif "tell me your name" in query:
            speak("I am VA. Your Virtual Assistant")

        elif "open" in query:
            openApp()

        
  
if __name__ == '__main__':
      
    # main method 
    Take_query()
