import time

from recognition import Recognizer
from voice import voice
from commands import Command


rec = Recognizer()
rec.stream.stop_stream()
voice.text_to_speech('Привет! Я голосовой ассистент')
time.sleep(0.5)
rec.stream.start_stream()
text_gen = rec.listen()
for text in text_gen:
    print(text)
    Command(text)
    time.sleep(0.5)
