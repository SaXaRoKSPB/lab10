import webbrowser
from voice import voice
import requests
from googletrans import Translator
import random, sys

translator = Translator()


def hello(text):
    sentence = [
        'И снова здравствуйте! О чём хотите поговорить?',
        'Как всегда готова к вашим заданиям!',
        'Чем сегодня будем заниматься?'
    ]
    answer = random.choice(sentence)
    voice.text_to_speech(answer)


def anecdot(text):
    URL = 'https://v2.jokeapi.dev/joke/Any?type=twopart'
    request_URL = requests.get(URL)
    anecdot_en = request_URL.json()
    anecdot_ru = translator.translate(anecdot_en['setup']+anecdot_en['delivery'], dest='ru')
    voice.text_to_speech(anecdot_ru.text)


def video(text):
    URL = [
        'https://www.youtube.com/watch?v=085sSdwvl2k',
        'https://www.youtube.com/watch?v=0sRiHF_VsUA',
        'https://www.youtube.com/watch?v=KN3IemyqJJw&t=176s',
        'https://www.youtube.com/watch?v=g-OQh_7fEWE',
        'https://www.youtube.com/watch?v=iiWTpcFwjDQ',
        'https://www.youtube.com/watch?v=RolHPRDBz2M',
    ]
    answer = webbrowser.open(random.choice(URL))
    voice.text_to_speech('Из вашего любимого! Наслаждайтесь!')


def work(text):
    webbrowser.open('https://www.youtube.com/watch?v=gEizosFZ-hs')
    voice.text_to_speech('Отличная музыка вам для активной работы! Если что зовите!')


def bye(text):
    sentence = [
        'И нова вы меня покидаете. Возвращайтесь поскорее!',
        'Удачи вам и хорошего дня!',
        'Жаль, что у вас есть что-то важнее, чем я',
    ]
    answer = random.choice(sentence)
    voice.text_to_speech(answer)
    sys.exit()