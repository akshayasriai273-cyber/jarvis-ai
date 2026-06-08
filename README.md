# Jarvis AI Voice Assistant

## Overview

Jarvis AI is a Python-based voice assistant that can listen to user commands, respond with AI-generated answers, speak responses aloud, open websites, and perform various desktop tasks.

## Features

* Voice command recognition
* AI-powered responses using Gemini API
* Text-to-Speech (gTTS)
* GUI interface
* Open websites and applications
* WhatsApp message support
* Smart conversation handling

## Technologies Used

* Python
* Google Gemini API
* SpeechRecognition
* gTTS
* Pygame
* Tkinter
* PyWhatKit
* PyAutoGUI
* python-dotenv

## Project Structure

* `jarvis.py` - Main assistant logic
* `jarvis_gui.py` - GUI interface
* `gemini_test.py` - Gemini API testing
* `gtts_test.py` - Text-to-speech testing
* `test_voice.py` - Voice recognition testing

## Installation

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the project:

```bash
py-3.11 jarvis.py
```

## Future Improvements

* Desktop application (.exe)
* Wake word detection ("Hey Jarvis")
* Chat history memory
* Advanced automation
* Multi-language support

## Author

Akshayasri
