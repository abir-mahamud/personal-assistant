from google_trans_new import google_translator
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

def talk(text):

    engine.say(text)
    engine.runAndWait()

def take_command():
    command = ''

    try:

        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source)
            print("listening: ")
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said: {}".format(command))

            translator = google_translator()
            translate_text = translator.translate(command, lang_tgt='bn')
            print(translate_text)
            # text = listener.recognize_google(audio, language="bn-BD")
            # print("Decoded Text : {}".format(text))
            if 'siri' in command:
                command = command.replace('siri','')
                talk(command)
    except:
        print("Couldn't Recognize your voice")
    return command

def run_siri():

    command = take_command()

    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', ())
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        print("That's what you said")

while True:
    run_siri()