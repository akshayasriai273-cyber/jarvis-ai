from gtts import gTTS
import pygame
import time
import os

pygame.mixer.init()

def speak(text, filename="voice.mp3"):
    tts = gTTS(text)
    tts.save(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()
    os.remove(filename)


speak("Hello Akshayasri")
time.sleep(1)

speak("How are you")
time.sleep(1)

speak("Goodbye")