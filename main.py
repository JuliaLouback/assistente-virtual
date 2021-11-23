import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import cv2

listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
                talk('I am listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()

                if 'alexa' in command:
                    command = command.replace('alexa', '')
    except:
        pass

    return command

def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('Current time is ' + time)
    elif 'write' in command:
        pywhatkit.text_to_handwriting(command, save_to='text.png')
        img = cv2.imread("text.png")
        cv2.imshow("Text to Handwriting", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    elif 'wikipedia' or 'what is' or 'who is' in command:
        command = command.replace('wikipedia', ' ').replace('what is', ' ').replace('who is', ' ')
        info = wikipedia.summary(command, 2)
        talk(info)

    else:
        talk("Please speak again")

    print(command)

while True:
    run_alexa()

