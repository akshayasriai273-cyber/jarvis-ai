import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser
import os
from datetime import datetime

r = sr.Recognizer()

def speak(text):
    print("SPEAKING:", text)

    tts = gTTS(text=text, lang="en")
    tts.save("jarvis_voice.mp3")

    playsound("jarvis_voice.mp3")

    # os.remove("jarvis_voice.mp3")

while True:

    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio).lower()

        print("You said:", text)

        if "hello" in text:
            reply = "Hello Akshayasri"

        elif "who are you" in text:
            reply = "I am Jarvis"

        elif "how are you" in text:
            reply = "I am fine. Thank you for asking."

        elif "open chrome" in text:
            os.startfile(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            )
            reply = "Opening Chrome"

        elif "time" in text:
            current_time = datetime.now().strftime("%I:%M %p")
            reply = f"The time is {current_time}"

        elif "open youtube" in text:
            webbrowser.open("https://www.youtube.com")
            reply = "Opening YouTube"

        elif "open whatsapp" in text:
            webbrowser.open("https://web.whatsapp.com")
            reply = "Opening WhatsApp"

        elif "search" in text:
            search_query = text.replace("search", "").strip()

            webbrowser.open(
                f"https://www.google.com/search?q={search_query}"
            )

            reply = f"Searching for {search_query}"

        elif "play" in text:
            song = text.replace("play", "").strip()

            webbrowser.open(
                f"https://www.youtube.com/results?search_query={song}"
            )

            reply = f"Playing {song}"

        elif "stop" in text:
            speak("Goodbye")
            break

        else:
            reply = "I did not understand"

        speak(reply)

    except Exception as e:
        print("Error:", e)