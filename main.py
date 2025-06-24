from RealtimeSTT import AudioToTextRecorder
import threading
from pygame import mixer
import os
import time
import random
import string
import pyautogui
import random

mixer.init(devicename="CABLE Input (VB-Audio Virtual Cable)")

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def replace_in_file(output_file, replacement_string):
    try:
        words = replacement_string.split() #splits the string into a list of words
        

        with open("template.ustx", 'r', encoding='utf-8') as file: #the template for the basic stuff of the file
            file_template = file.read()

        with open("word.txt", 'r', encoding='utf-8') as file: #the template for adding a new voice segment
            speech_template = file.read()

        with open(f"temp\{output_file}", 'w', encoding='utf-8') as output_file:
            total_dur = 0 #the total duration of the file, as this number is updated it will be used to figure out the position of each segment
            output_file.write(file_template) #adds basic file stuff
            for i in range(len(words)): #loops through the list of words
                segment = speech_template #copies the template so we dont accidently override the original
                segment = segment.replace("POS__", str(total_dur))
                segment = segment.replace("WORD__", words[i])
                words[i] = words[i].replace(".","").replace(",","").replace("?","").replace("!","").replace("'","")
                duration = len(words[i])*90 #calculates a duration for how long the word should be said based off of the length of the word
                segment = segment.replace("DUR__", str(duration))
                total_dur = total_dur + duration
                segment = segment.replace("TONE__", str(random.randint(60,70)))
                output_file.write("\n"+segment) #adds new segment
            output_file.write("\nwave_parts: []") #finalizes file by adding stuff that comes after the segments

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    print("Wait until it says 'speak now'")

    recorder = AudioToTextRecorder(language="en")
    
    while True:
        text = recorder.text()
        print(text)
        output_file = f'{generate_random_string()}.ustx'
        replace_in_file(output_file, text)
        #t = threading.Thread(target=replace_in_file, args=(output_file, search_phrase, text,))
        #t.start()