import speech_recognition
import pyttsx3
import pywhatkit
import datetime
import wolframalpha
import time

recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()
client = wolframalpha.Client("Enter wolframalpha app id")


def talk(text):
    engine.say(text)
    engine.runAndWait()

print("How would you like me to call you? Please type below")
talk('How would you like me to call you? Please type below')
choice = input("Enter here")

while True:
    print("I am listening" + ' ' + choice)
    talk("I am listening" + ' ' + choice)

    def error():
        print("I didn't quite understand" + ' ' + choice)
        talk("I didn't quite understant")

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
                print("playing" + ' ' + song + ' ' + choice)
                talk('playing' + song + ' ' + choice)
                pywhatkit.playonyt(song)
            except:
                error()
        elif 'you there' in command:
            try:
                print("I am always here for you!" + ' ' + choice)
                talk('I am always here for you!' + ' ' + choice)
            except:
                error()
        elif 'created you' in command:
            try:
                print("Tony Chung is the creator of mine"+ ' ' + choice)
                talk('Tony Chung is the creator of mine'+ ' ' + choice)
            except:
                error()
        elif 'made you' in command:
            try:
                print("Tony Chung is the creator of mine"+ ' ' + choice)
                talk('Tony Chung is the creator of mine'+ ' ' + choice)
            except:
                error()
        elif 'your day' in command:
            try:
                print("My day has been so far great, Thankyou for asking!"+ ' ' + choice)
                talk('My day has been so far great, Thankyou for asking!'+ ' ' + choice)
            except:
                error()
        elif 'Hi' in command:
            try:
                print("Hello" + ' ' + choice)
                talk('Hello' + ' ' + choice)
            except:
                error()
        elif 'time' in command:
            try:
                time = datetime.datetime.now().strftime('%H:%M')
                print(time + ' ' + choice)
                talk('The current time is' + time + ' ' + choice)
            except:
                error()
        elif 'date' in command:
           try:
                dt_today = datetime.datetime.today()
                date = (dt_today.strftime('%Y-%m-%d'))
                print(date + " " + ' ' + choice)
                talk('The current date is' + date + ' ' + choice)
           except:
               error()
        else:
            try:
                res = client.query(command)
                print((next(res.results).text + ' ' + choice))
                talk(next(res.results).text + ' ' + choice)
            except:
                error()

    run_mark()
    time.sleep(1.3)
