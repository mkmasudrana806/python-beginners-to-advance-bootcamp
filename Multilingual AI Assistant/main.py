import speech_recognition as sr # recognize our speech 
import logging
import os
from gtts import gTTS
import google.generativeai as genai
import streamlit as st


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


# text to voice
def text_to_speech(text):
    ttx = gTTS(text=text, lang='en')
    ttx.save('speech.mp3')


# gemini model configure
def gemini_model(user_input):
    genai.configure(api_key="AIzaSyD-TpraSOLFina4VVLvcLFcj4UcAKyWnh8")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content('in short' + user_input)
    results = response.text
    return results


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
        return 'What is python?'
    


# create a server
def main():
    st.title('Multilingual AI Assistant')
    
    if st.button('Ask me anything'):
        with st.spinner('Listening...'):
            text = takeCommand()
            gemini_response = gemini_model(text)
            text_to_speech(gemini_response)
            
            # display audio player and download link
            audio_file = open("speech.mp3", "rb")
            audio_bytes = audio_file.read()
            
            st.text_area(label='Response: ', value=gemini_response, height=350)
            st.audio(audio_bytes, format='audio/mp3')
            st.download_button(label='Download Speech', data=audio_bytes, file_name='speech.mp3', mime='audio/mp3')
    
main() # in terminal: streamlit run main.py

# text = takeCommand()
# response = gemini_model(text)
# print(response)
# text_to_speech(response)

#api key: AIzaSyD-TpraSOLFina4VVLvcLFcj4UcAKyWnh8