# import os
import webbrowser
import sys
import subprocess
import voice
from playsound import playsound
import random

try:
    import requests
except:
    pass


def browser():
    webbrowser.open('https://youtube.com', new=2)


def game():
    try:
        subprocess.Popen('D:/Games/Watch Dogs 2/bin/WatchDogs2.exe')
    except:
        voice.speaker('Путь на файл только укажи сначала')


def offpc():
    print('пк был бы выключен, но команде # в коде мешает;)))')


def music_hard():
    webbrowser.open("https://youtu.be/CP1cdqEERjU?t=150", new=2)


def offBot():
    sys.exit()


def time():
    playsound("time_is.mp3")


def meme():
    a = random.randint(1, 3)
    if a == 1:
        playsound("mem_ti_autor.mp3")
    elif a == 2:
        playsound("ves-mir.mp3")
    elif a == 3:
        playsound("zanimaytes-sportom.mp3")


def passive():
    pass
