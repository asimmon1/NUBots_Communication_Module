from time import sleep
import wave
from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError

model = "google"


# Used to recognize a microphone clip
def callback(recognizer, source):
    # print(type(source))
    recognized = "Null"
    with open('new_audio.wav', 'wb') as file:
        file.write(source.get_wav_data())
    try:

        if model == "google":
            recognized = recognizer.recognize_google(source)
        else:
            recognized = recognizer.recognize_sphinx(source)

        print("You said: ", recognized)
        file.close()


    except UnknownValueError:
        file.close()
    return recognized


# Listens for speech
def listen():
    recog = Recognizer()
    mic = Microphone()

    with mic:
        recog.adjust_for_ambient_noise(mic)
        print('Listening.....')
        recog.pause_threshold = 2
        recog.energy_threshold = 4000
        audio = recog.listen(mic)
        recognized = callback(recog, audio)
        if recognized != "Null":
            return recognized
        else:
            return "Null"


# analyses a given wav file
def analyseFile(file):
    recog = Recognizer()
    audio_file = AudioFile(file)

    with audio_file as af:
        audio_content = recog.record(af)

    try:
        recognized = recog.recognize_sphinx(audio_content)
        print("You said: ", recognized)

    except UnknownValueError:
        print("Cannot hear input value  ")
        recognized = "NULL"
    return recognized

# used for continuous listening


# test('tester.mp3')
