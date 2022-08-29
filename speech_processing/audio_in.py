import json

from vosk import Model, KaldiRecognizer
from pyaudio import PyAudio, paInt16

model = Model("vosk-model-en-us-0.21")
recognizer = KaldiRecognizer(model, 16000)
mic = PyAudio()
stream = mic.open(format=paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)


def hear():
    return_string_list = []
    while True:
        data = stream.read(1024)
        if not recognizer.AcceptWaveform(data):
            break
        return_string_list.append(json.loads(recognizer.Result())['text'])
    return " ".join(return_string_list)
