"""
Real-Time Text to speech Engine (TTS)
Dependencies: 'pyttsx' module
For querres conatct: dknaix.github@gamil.com
"""

import pyttsx3

def TTS(text):  #real_time TTS("string")
    print("TTS RECV:"+text)
    engine = pyttsx3.init()

    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) #changing index changes voices but ony 0 and 1 are working here

    engine.say(text)
    engine.runAndWait()


while 1:
    TTS(input("Enter text:"))
