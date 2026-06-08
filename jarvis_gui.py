import customtkinter as ctk
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import threading
import time

# ---------------- UI ----------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("JARVIS AI - AUTO MODE")
app.geometry("500x600")

title = ctk.CTkLabel(app, text="JARVIS AUTO LISTEN", font=("Arial", 20, "bold"))
title.pack(pady=20)

chat_box = ctk.CTkTextbox(app, width=450, height=400)
chat_box.pack(pady=10)

# ---------------- CHAT ----------------
def add(text):
    chat_box.insert("end", text + "\n")
    chat_box.see("end")

# ---------------- AI ----------------
def get_response(text):
    text = text.lower()

    if "hello" in text:
        return "Hello! I am listening"

    elif "time" in text:
        return datetime.now().strftime("Time is %I:%M %p")

    elif "date" in text:
        return datetime.now().strftime("Today is %d %B %Y")

    elif "who are you" in text:
        return "I am your Jarvis assistant"

    elif "stop" in text:
        return "Stopping voice mode"

    else:
        return "I am still learning"

# ---------------- SPEAK ----------------
def speak(text):
    def run():
        engine = pyttsx3.init()
        engine.setProperty('rate', 170)
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target=run, daemon=True).start()

# ---------------- LISTEN LOOP ----------------
running = False

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        while running:
            try:
                add("🎤 Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
                text = r.recognize_google(audio)

                add("You: " + text)

                response = get_response(text)

                add("Jarvis: " + response)

                speak(response)

                if "stop" in text.lower():
                    stop_listening()
                    break

            except:
                continue

# ---------------- START / STOP ----------------
def start_listening():
    global running
    running = True
    add("Jarvis started listening...")
    threading.Thread(target=listen, daemon=True).start()

def stop_listening():
    global running
    running = False
    add("Jarvis stopped.")

# ---------------- BUTTONS ----------------
start_btn = ctk.CTkButton(app, text="Start Listening", command=start_listening)
start_btn.pack(pady=10)

stop_btn = ctk.CTkButton(app, text="Stop", command=stop_listening)
stop_btn.pack(pady=10)

print("AUTO JARVIS STARTED")
app.mainloop()