import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
impot smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour<12:
    speak("Good Morning")

   elif hour>=12 and hour<18:
    speak("Good Afternoon!")

   else:
    speak("Good Evening:")

    speak("I am Jarvis Sir, PLease tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
        #print(e)

        print("Say that again please...")
        return "None"
    return query
def send Email(do,content):
server = smtp.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('youremail@gmail.com', 'your-password')
server.sendmail('youremail@gmail.com', to, content)
if __name__ =="__main__":
    #wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
    
    # Logic for executing task based on query
    if 'wikipedia' in query:
        speak('Searching wikipedia...')
        query = query.replace("wikipedia","")
        result = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(result)
        speak(result)

    elif'open youtube' in query:
        webbrowser.open("youtube.com")
        
    elif'open youtube' in query:
        webbrowser.open("google.com")

    elif'open stackoverflow' in query:
        webbrowser("stackoverflow.com")

    elif 'the time' in query:
        strTime = datetime.datetime.now(). strftime("%H:%N:%S")
        speak(f"Sir, the time is {strTime}")

    elif ' email to ratan' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            to = "ratanyourEmail@gmail.com"
            sendEmail(to, content)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry my friend ratan. I am not able to send email")



