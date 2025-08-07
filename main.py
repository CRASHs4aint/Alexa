import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary  # Make sure this is a custom Python file with a `music` dict or function.
import requests

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="a8112ae33be04f2f8bf9f45acd5fbd89"

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
    elif c.lower().startswith("play"):
       
            song = c.lower().split(" ")[1]  # Get the song name after "play"
            link= musicLibrary.music[song]  # Assuming music is a dict with callable song functions
            webbrowser.open(link)
    elif"news" in c.lower()
        r=requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=a8112ae33be04f2f8bf9f45acd5fbd89")
        

if __name__ == "__main__":
    speak("Initializing Alexa.......")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)
            print(f"Heard: {word}")

            if word.lower() == "alexa":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Alexa Active...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                try:
                    command = recognizer.recognize_google(audio)
                    print(f"Command: {command}")
                    processCommand(command)
                except sr.UnknownValueError:
                    speak("Sorry, I didn't catch that.")
                except sr.RequestError as e:
                    speak("Speech service error.")
                    print(f"Request error: {e}")

        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase")
        except Exception as e:
            print(f"Error: {e}")
