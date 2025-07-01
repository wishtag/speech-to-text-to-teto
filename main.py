from RealtimeSTT import AudioToTextRecorder
import random
import string
import pyautogui
import os
import time

def generate_random_string(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def replace_in_file(output_file, replacement_string):
    try:
        words = replacement_string.split()

        with open("templates\\template.txt", 'r', encoding='utf-8') as file:
            file_template = file.read()

        with open("templates\\word.txt", 'r', encoding='utf-8') as file:
            speech_template = file.read()

        updated_content = file_template
        with open(f"temp\{output_file}", 'w', encoding='utf-8') as output_file:
            total_dur = 0
            for i in range(len(words)):
                segment = speech_template

                segment = segment.replace("POS__", str(total_dur))

                segment = segment.replace("WORD__", words[i])

                words[i] = words[i].replace(".","").replace(",","").replace("?","").replace("!","").replace("'","")
                
                duration = len(words[i])*100
                segment = segment.replace("DUR__", str(duration))
                
                total_dur = total_dur + duration

                segment = segment.replace("TONE__", str(random.randint(60,70)))
                
                updated_content = updated_content + "\n" + segment
            
            updated_content = updated_content + "\nwave_parts: []"
            output_file.write(updated_content)

    except Exception as e:
        print(f"An error occurred: {e}")

def play(file):
    path = os.path.abspath(f"temp\{file}")

    pyautogui.hotkey('ctrl', 'o')
    time.sleep(1)
    pyautogui.typewrite(path)
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.press('space')
    os.remove(path)

if __name__ == '__main__':
    print("Wait until it says 'speak now'")

    recorder = AudioToTextRecorder(language="en")

    while True:
        text = recorder.text()
        print(text)
        output_file = f'{generate_random_string()}.ustx'
        replace_in_file(output_file, text)
        play(output_file)