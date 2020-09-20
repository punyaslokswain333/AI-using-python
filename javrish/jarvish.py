import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning Punya")
    elif hour>=12 and hour<18:
        speak("good afternoon ")
    elif hour>=18 and hour<=21:
        speak("good evening Punya SIR")
    else: 
        speak("good night babe")
    speak(" i am jarvish sir!!! please tell me that how can i help you")
def takeCommand():
    # take microphone input and return as string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.................")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing>>>>>>>>>>>>>>")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("say that again plese:) :) :) :) ")
        return"None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic according  to query
        if 'wikipedia' in query:
            speak('searching wikipedia sir....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("accrding to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak('opening youtube sir....')
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            speak('opening google sir....')
            webbrowser.open("google.com")
        
        elif 'play music in gaana' in query:
            speak('opening google sir....')
            webbrowser.open("gaana.com")
        elif 'open idea innovation cell' in query:
            speak('opening idea innovation cell sir....')
            webbrowser.open("iic-vssut.org")