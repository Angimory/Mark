import speech_recognition
import pyttsx3
import pywhatkit
import datetime
import wolframalpha

recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()
client = wolframalpha.Client("Enter Wolfram AppID")

def talk(text):
    engine.say(text)
    engine.runAndWait()

print('I am listening sir')
talk('I am listening sir')

def error():
    print("I didn't quite understant sir")
    talk("I didn't quite understant sir")
    exit()

def receive_command():
    try:
        with speech_recognition.Microphone() as source:
            voice = recognizer.listen(source)
            command = recognizer.recognize_google(voice)
            command = command.lower()
            if 'Mark' in command:
                try:
                    command = command.replace('Mark', '')
                    command = command.replace('.', '')
                    print(command)
                except:
                    error()
    except:
        error()
    return command

def run_mark():
    command = receive_command()
    if 'play' in command:
        try:
            song = command.replace('play', '')
            print("playing" + ' ' + song)
            talk('playing' + song)
            pywhatkit.playonyt(song)
        except:
            error()
    elif 'you there' in command:
        try:
            print("I am always here for you sir!")
            talk('I am always here for you sir!')
        except:
            error()
    elif 'created you' in command:
        try:
            print("Tony Chung is the creator of mine sir!")
            talk('Tony Chung is the creator of mine sir!')
        except:
            error()
    elif 'made you' in command:
        try:
            print("Tony Chung is the creator of mine sir!")
            talk('Tony Chung is the creator of mine sir!')
        except:
            error()
    elif 'your day' in command:
        try:
            print("My day has been so far great sir! Thankyou for asking!")
            talk('My day has been so far great sir! Thankyou for asking!')
        except:
            error()
    elif 'Hi' in command:
        try:
            print("Hello sir!")
            talk('Hello sir!')
        except:
            error()

    elif 'time' in command:
        try:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time + " " + "sir")
            talk('The current time is' + time + 'sir')
        except:
            error()
    elif 'date' in command:
       try:
            dt_today = datetime.datetime.today()
            date = (dt_today.strftime('%Y-%m-%d'))
            print(date + " " + "sir")
            talk('The current date is' + date + 'sir')
       except:
           error()
    else:
        try:
            res = client.query(command)
            print((next(res.results).text +" sir"))
            talk(next(res.results).text + "sir")
        except:
            error()

run_mark()