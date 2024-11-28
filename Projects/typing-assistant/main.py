from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time
import httpx
from string import Template

controller = Controller()

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate" 
OLLAMA_CONFIG = {
    "model": "Mistral:7B-Instruct",
    "keep_alive": "10m",  # Keep alive duration in string format
    "stream": False
}

PROMPT_TEMPLATE = Template(
    """Fix all typos and casing and punction in this text, but perserve all new line characters and line format if multi line:
    
    $text
    
    Return only the corrected text, don't include a preamble
    """
)

def fix_text(text):
    prompt = PROMPT_TEMPLATE.substitute(text=text)
    response = httpx.post(OLLAMA_ENDPOINT,
                          json={'prompt':prompt, **OLLAMA_CONFIG},
                          headers={'Content-Type': 'application/json'},
                          timeout = 100)
    if response.status_code != 200:
        return None
    return response.json()["response"].strip()
    

def fix_current_line():
    #shift + down_arrow
    controller.press(Key.shift)
    controller.press(Key.down)

    controller.release(Key.shift)
    controller.release(Key.down)
    fix_selection()

def fix_selection():
    # 1. Copy to clipboard
    with controller.pressed(Key.ctrl):
        controller.tap('c')
    # 2. get th text from the clipboard
    time.sleep(0.1)
    text = pyperclip.paste()
    # 3. fix the text
    fixed_text = fix_text(text)

    # 4. copy back to the clipboard
    pyperclip.copy(fixed_text)
    time.sleep(0.1)
    # 5. Insert text 
    with controller.pressed(Key.ctrl):
        controller.tap('v')

def on_f9():
    print("f9 pressed")
    fix_current_line()
 
def on_f10():
    print("f10 pressed")
    fix_selection()

def on_exit():
    print("Exiting...")
    quit() # Returning False stops the listener


with keyboard.GlobalHotKeys({
        '<f9>': on_f9,
        '<f10>': on_f10,
        '<f1>': on_exit}) as h:
    h.join()
