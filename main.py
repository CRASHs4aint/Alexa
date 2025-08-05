import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

#pip install pocketsphinx

recognizer= sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c): 
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")  
    elif c.lower() .startswith("play"):
         song =c.lower().split("")[1]
         musicLibrary.music[song]       
    
    
if __name__== "__main__":
    speak("Initializing Alexa.......")
    
    #listen for the woke word "alexa"
         # obtain audio from the microphone
    
    while True:
        
        try:
          r = sr.Recognizer()
          with sr.Microphone() as source:
           print("Listening for wake word...")
          audio = r.listen(source,timeout=3,phrase_time_limit=2)
        except Exception as e:
         print(f"Error: {e}") 
    
        word = r.recognize_google(audio)
        print(f"Heard:{word}")
        if(word.lower() == "alexa"):
           speak("ya")
           #listen for command 
           with sr.Microphone() as source:
            print("Alexa Active...")
           audio = r.listen(source ,Timeout=5,phrase_time_limit=5)
           
           command = r.recognize_google(audio)
           print(f"command:{command}")
#            processCommand(command)
# except Exception as e:
# print(f"Error: {e}")   
           
#         except sr.waitTimeoutError:
#         continue #Ignore and continue listening
#  except sr.UnknownValueError:
# print("Sorry, I didn't catch that.")

    