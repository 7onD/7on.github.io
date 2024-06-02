# Голосовой ассистент Gibbs (Гиббс) 1.0 BETA
import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime
import pyautogui as pg
import time
import random
import pyautogui as pg
import pyaudio
from bot import bot

# настройки
opts = {
    "alias": ("Гибс", "гипс", "Гипс",'гибс','джо','Джо','Джошами','жо','Жо','кипс','Кипс','Кибс','Кибс', 'денис'),
    "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси'),
    "cmds": {
        "ctime": ('текущее время', 'сейчас времени', 'который час'),
        "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты'),
        "git": ('протокол гит', 'протокол git', 'protocol git', 'protocol gid', 'протокол гид', 'протокол gid'),
        'hello': ('привет', 'hello', 'приветик', 'приветики'),
        'hay': ('как дела', 'как сам', 'как ты', 'how are you','хав ар ю'),
        'quit': ('протокол ноль', 'протокол 0', 'protocol 0', 'protocol nol', 'protocol ноль', 'закройся', 'уйди', 'пока', 'пака'),
        'bad': ('ты дурачёк', 'дурачёк', 'дэбил')
    }
}


# функции
def speak(what):
    print(what)
    speak_engine.say(what)
    speak_engine.runAndWait()
    speak_engine.stop()


def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language="ru-RU").lower()
        print("[log] Распознано: " + voice)

        if voice.startswith(opts["alias"]):
            # обращаются к Гиббсу
            cmd = voice

            for x in opts['alias']:
                cmd = cmd.replace(x, "").strip()

            for x in opts['tbr']:
                cmd = cmd.replace(x, "").strip()

            # распознаем и выполняем команду
            cmd = recognize_cmd(cmd)
            execute_cmd(cmd['cmd'])

    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")


def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt

    return RC


def execute_cmd(cmd):
    if cmd == 'ctime':
        now = datetime.datetime.now()
        speak("Сейчас " + str(now.hour) + ":" + str(now.minute))
        print("Слушаю")
    elif cmd == 'quit':
        speak('Завершаю работу.')
        pg.hotkey("alt",'f4')
    elif cmd == "git":
        speak("Протокол Git запущен!")
        os.system("C:\\Users\\sd051\\Desktop\\!Projects\\PyAutoGUI\\bat\\git_pusher.bat")
    elif cmd == 'stupid1':
        speak("Мой разработчик не научил меня анекдотам ... Ха ха ха")
        print("Слушаю")
    else:
        speak(bot(cmd))

# запуск
r = sr.Recognizer()
m = sr.Microphone(device_index=4)

with m as source:
    r.adjust_for_ambient_noise(source)

speak_engine = pyttsx3.init()

# Только если у вас установлены голоса для синтеза речи!
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[0].id)


speak(random.SystemRandom().choice(["Голосовой ассистент Гиббс запустился. Я снова с вами, сэр!", 'Голосовой ассистент Гиббс запустился. Здравствуйте, сэр!']))

while True:
    with m as source:
        print("Слушаю")
        audio = r.listen(source)

    callback(r, audio)
    time.sleep(0.1)