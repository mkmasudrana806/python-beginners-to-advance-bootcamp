import speech_recognition as sr # recognize our speech 
import pyttsx3 # text to speech (tts3)
import logging
import os
import datetime
import webbrowser # for open any kind of browser
import wikipedia

# this is logger for the application
LOG_DIR = 'logs'
LOG_FILE_NAME = 'application.log'

os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig (
    filename=log_path,  
    format = "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
    )

# taking the male voice form my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') # get all voices
engine.setProperty('voices', voices[0].id) # set voice


# text to voice
def speak(text):
    """This function will convert text to a voice 

    Args:
        text
    Returns:
        voice
    """
    engine.say(text)
    engine.runAndWait()



# take command function
def takeCommand():
    """This function take voice command and recognize

    Returns:
        text as query
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print('Recongning...')
        query = r.recognize_google_cloud(audio, language='en-in')
        print(f"User said {query}\n")
    except Exception as e:
        logging.info(e)
        return "What is python?"
    
    
# this function will wish you
def wish_me():
    hour = (datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak('Good Morning sir! How are you doing')
    
    elif hour >= 12 and hour <=18:
        speak('Good afternoot sir! How are you doing?')
    
    elif hour > 18 and hour <=24:
        speak('Good Evening sir! What are you doing')
    
    else:
        speak('I am JARVIS. Tell me sir, how can i help you?')
    
wish_me()

# run application infinite time
while True:
    query = takeCommand().lower()
    
    if "time" in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {time}")
        
    elif "name" in query:
        speak("My name is JARVIS")
        
    elif "exit" in query:
        speak('Goodbye sir')
        exit()
        
    elif "open google" in query:
        speak("ok sir, openning google..")
        webbrowser.open_new_tab("www.google.com")
        
    elif "open facebook" in query:
        speak("ok sir, openning facebook..")
        webbrowser.open_new_tab("www.facebook.com")
        
    elif "python" in query:
        speak('Python is a high level programming language, that uses interpreter. it is well known for versatile, readability, large libraries support and big community')
        
    elif 'wikipedia' in query:
        try:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak('According to wikipedia')
            speak(results)
        except Exception as e:
            print('Nothing is found in your query sir')
            speak('Nothing is found in your query sir')
    else:
        speak('goodbye sir')
        exit()