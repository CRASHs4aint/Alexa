import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer= sr.Recognizer
engine = pyttsx3.init()

def speak(text):
    engine.say("text")
    engine.runAndWait()
    
if __name__== "_main_":
    speak("Initializing Alexa.......")
    while True:
         #listen for the woke word "alexa"
         # obtain audio from the microphone
         r = sr.Recognizer()
         with sr.Microphone() as source:
          print("Say something!")
          audio = r.listen(source)

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))

   