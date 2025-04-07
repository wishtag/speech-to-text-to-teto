from RealtimeSTT import AudioToTextRecorder
import pyttsx3
import threading
from pygame import mixer
import os
import time
import random
import string
import pyautogui

mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")

engine = pyttsx3.init()
engine.setProperty('rate', 200)

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def replace_in_file(output_file, search_phrase, replacement_string):
    try:
        with open("template.ustx", 'r', encoding='utf-8') as file:
            content = file.read()

        updated_content = content.replace(search_phrase, replacement_string)

        with open(f"temp\{output_file}", 'w', encoding='utf-8') as output_file:
            output_file.write(updated_content)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    print("Wait until it says 'speak now'")

    recorder = AudioToTextRecorder(language="en")

    search_phrase = "REPLACE_ME"
    
    while True:
        text = recorder.text()
        print(text)
        output_file = f'{generate_random_string()}.ustx'
        replace_in_file(output_file, search_phrase, text)
        #t = threading.Thread(target=replace_in_file, args=(output_file, search_phrase, text,))
        #t.start()
