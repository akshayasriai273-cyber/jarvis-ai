import speech_recognition as sr
import webbrowser
import os
import time
import pygame
from gtts import gTTS
from datetime import datetime
import pyautogui
import pywhatkit
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# PUT YOUR NEW API KEY HERE
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

print("JARVIS AI VERSION 4.1 - READY")

pygame.mixer.init()

def speak(text):
    print("SPEAKING:", text)

    filename = "voice.mp3"

    try:
        tts = gTTS(text=text, lang="en")
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()

    finally:
        if os.path.exists(filename):
            try:
                os.remove(filename)
            except:
                pass

r = sr.Recognizer()

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
documents_path = os.path.join(os.path.expanduser("~"), "Documents")
memory_file = "memory.txt"

while True:

    try:
        with sr.Microphone() as source:

            print("Listening...")

            r.adjust_for_ambient_noise(source, duration=0.5)

            audio = r.listen(
                source,
                timeout=10,
                phrase_time_limit=8
            )

        text = r.recognize_google(audio).lower().strip()

        print("You said:", text)

        if "hello" in text:
            reply = "Hello Akshayasri"

        elif "who are you" in text:
            reply = "I am Jarvis"

        elif "how are you" in text or "how r u" in text:
            reply = "I am doing great"

        elif "open chrome" in text or text == "chrome":
            os.startfile(
                r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            )
            reply = "Opening Chrome"

        elif "open youtube" in text or text == "youtube":
            webbrowser.open("https://www.youtube.com")
            reply = "Opening YouTube"

        elif "open whatsapp" in text or text == "whatsapp":
            webbrowser.open("https://web.whatsapp.com")
            reply = "Opening WhatsApp"

        elif "open calculator" in text or text == "calculator":
            os.system("calc")
            reply = "Opening Calculator"

        elif "open notepad" in text or text == "notepad":
            os.system("notepad")
            reply = "Opening Notepad"

        elif "vscode" in text or "vs code" in text or text == "code":
            os.startfile(
                r"C:\Users\ravis\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            )
            reply = "Opening Visual Studio Code"

        elif "take screenshot" in text or text == "screenshot":
            pyautogui.screenshot().save("screenshot.png")
            reply = "Screenshot saved successfully"

        elif "shutdown" in text or text == "shutdown": 
           os.system("shutdown /s /t 5")
           reply = "Shutting down system"

        elif "restart" in text or text == "restart":
           os.system("shutdown /r /t 5")
           reply = "Restarting system"

    

        elif "open downloads" in text or text == "downloads":
            os.startfile(downloads_path)
            reply = "Opening Downloads folder"

        elif (
            "open document" in text
            or "open documents" in text
            or text == "document"
            or text == "documents"
        ):
            os.startfile(documents_path)
            reply = "Opening Documents folder"
        elif text.startswith("calculate"):

          expression = text.replace("calculate", "", 1).strip()

          expression = expression.replace("x", "*")
          expression = expression.replace("into", "*")

          try:
           result = eval(expression)
           reply = f"The answer is {result}"

          except:
           reply = "Sorry, I could not calculate that." 
        elif text.startswith("take note"):

          note = text.replace("take note", "", 1).strip()

          if note:
            with open("notes.txt", "a", encoding="utf-8") as f:
             f.write(note + "\n")

             reply = "Note saved successfully"

          else:
               reply = "What note should I save?" 
        elif text.startswith("play"):

           song = text.replace("play", "", 1).strip()

           if song:
              pywhatkit.playonyt(song)
              reply = f"Playing {song}"

           else:
              reply = "What should I play?"
        elif text.startswith("remember"):

          memory = text.replace("remember", "", 1).strip()

          if memory:
           with open(memory_file, "a", encoding="utf-8") as f:
            f.write(memory + "\n")

           reply = "I will remember that."

          else:
           reply = "What should I remember?"   
        elif "show memory" in text or text == "memory":


            try:
               with open(memory_file, "r", encoding="utf-8") as f:
                memories = f.read()

                if memories.strip():
                 reply = memories[:300]
                else:
                 reply = "I do not remember anything yet."

            except:
             reply = "Memory file not found."

            

        elif "time" in text:
           reply = datetime.now().strftime(
                "The current time is %I:%M %p"
            )

        elif "date" in text:
            reply = datetime.now().strftime(
                "Today is %d %B %Y"
            )

        elif text.startswith("search"):
            query = text.replace("search", "", 1).strip()

            if query:
                webbrowser.open(
                    f"https://www.google.com/search?q={query}"
                )
                reply = f"Searching for {query}"
            else:
                reply = "What should I search for?"

        elif text.startswith("play"):
            song = text.replace("play", "", 1).strip()

            if song:
                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={song}"
                )
                reply = f"Playing {song}"
            else:
                reply = "What should I play?"

        elif (
            text == "stop"
            or text == "exit"
            or text == "quit"
            or "stop jarvis" in text
        ):
            speak("Goodbye")
            break

        else:
            print("COMMAND NOT FOUND - USING GEMINI")

            try:
                response = model.generate_content(text)

                if hasattr(response, "text") and response.text:
                    reply = response.text[:300]
                else:
                    reply = "I did not get a response."

            except Exception as e:
                print("Gemini Error:", e)
                reply = "Sorry, Gemini is unavailable."

        speak(reply)

    except sr.WaitTimeoutError:
        print("No speech detected")

    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError:
        print("Speech recognition service unavailable")

    except Exception as e:
        print("Error:", repr(e))

        