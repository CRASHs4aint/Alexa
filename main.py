import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary  # Make sure this is a custom Python file with a `music` dict or function.

# Initialize recognizer and speech engine
recognizer = sr.Recognizer()
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
    elif c.lower().startswith("play"):
        try:
            song = c.lower().split(" ", 1)[1]  # Get the song name after "play"
            speak(f"Playing {song}")
            musicLibrary.music[song]()  # Assuming music is a dict with callable song functions
        except Exception as e:
            speak("Sorry, I couldn't find that song.")
            print(f"Music error: {e}")
    else:
        speak("Sorry, I didn't understand that command.")

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
