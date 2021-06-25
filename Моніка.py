# Голосовий асистент Моніка 1.0 BETA
import os
import time
import datetime
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
from random import randrange
import webbrowser
import wikipedia

opts = {
    "alias": ('моника', 'монька', 'моня', 'моська'),
    "tbr":('скажи','расскажи','покажи','сколько','произнеси','включи','открой'),
    "cmds": {
        "ctime": ('сколько времени','текущее время','которий час','сейчас времени'),
        "stupid": ('расскажи ','рассмени меня','ти знаешь анегдоты','мнэ грусно','пошути'),
        "youtube":('врубай ютуб','хочу послушать музику'),
        "fucking": ('ти дурна', 'дура'),
        "searching":('найди','поищи','мнэ нужно найти','включи поиск')
        }
    }

#функції
def speak(what):
    print (what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()

def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
         #звернення до Моніка
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()
            
            #розпізнавання і виконання команд
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

                
    except sr.UnknownValueError: 
        print("[log] Голос не распознан!")
    except sr.RequestError as e: 
        print("[log] неизвесная ошибка, провертье интернет!")

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c,v in opts['cmds'].items():
        for x in v:
            vrt = fuzz.ratio(cmd, x) 
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC
                
def execute_cmd(cmd):
    if cmd == 'ctime':
        #говорить час
        now = datetime.datetime.now()
        speak("Я тебе шо Биг Бен.... шучу")
        speak("сейчас " + str(now.hour) + ":" + str(now.minute))

    elif cmd == 'stupid':
        #розказати
        x = range(7)
        try:
            switch(x)
        except case(0):
            speak("Мой розработчик не научил меня анекдотам....Ха Ха Ха")
        except case(1):
            speak("Черепахи дышат попой...ги")
        except case(2):
            speak("В моём мире живут только пони...Они питаются райдугой и какают бабочками")
        except case(3):
            speak("Я всьо могу. Молчать можешь? Всьо могу молчать - не могу...")
        except case(4):
            speak("Питомцы - это такие животные которих не едят. А...Ми називаэм их детьми")
        except case(5):
            speak("Ну подумаєш - куснул по-дружески за попу! На, укуси меня! ")
        except case(6):
            speak("Если чайка летит жопой вперед значит ветер очень сильный... хи хи")
            
    elif cmd == 'youtube':
        #включає ютуб
        webbrowser.open('youtube.com/watch?v=xGvIdbB67Qs&ab_channel=JorgeGonzalezJorgeGonzalez', new=2)
        
    elif cmd =='fucking':
        speak("С таким коротентким ходотком я бы вёл себя поскромнее, парень.")

    elif cmd == 'saerching':
        ny = wikipedia.page(source)
            
    else:
        print('Команда не розпізнана повторіть')

#запуск
r= sr.Recognizer()
m= sr.Microphone(device_index = 1)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()
languages.Russian.use_pseudo_english= True


# тільки якщо встановлені голоса для ситезу мовлення
voices= speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)

speak("Добрый день")
speak("Моника слушает")

stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)


        
