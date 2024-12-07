from tkinter import *
import httpx
from string import Template

root = Tk()
root.geometry("800x1000")
input_prompt = None

OLLAMA_ENDPOINT = "http://localhost:11434/api/generate" 
OLLAMA_CONFIG = {
    "model": "Mistral:7B-Instruct",
    "keep_alive": "10m",  # Keep alive duration in string format
    "stream": False
}

PROMPT_TEMPLATE = Template(
    """$prompt
    
    $text
    
    Return only the response, don't include a preamble
    """
)

NO_TEXT_PROMPT_TEMPLATE = Template(
    """$prompt
    
    Return only the response, don't include a preamble
    """
)

def run(input_prompt):
    text=my_text.get(1.0, END)
    if input_prompt == None:
       #  my_label.config(text='Please provide a prompt.')
        print('please provide a prompt')
    if text == None:
        prompt = NO_TEXT_PROMPT_TEMPLATE.substitute(prompt=input_prompt)
        response = httpx.post(OLLAMA_ENDPOINT,
                              json={'prompt':prompt, **OLLAMA_CONFIG},
                              headers={'Content-Type': 'application/json'},
                              timeout=100)
        if response.status_code !=200:
            print('something went wrong')
        my_label.config(text=response.json()["response"].strip())
        return True
    else:
        prompt = PROMPT_TEMPLATE.substitute(prompt=input_prompt, text=text)
        response = httpx.post(OLLAMA_ENDPOINT,
                          json={'prompt':prompt, **OLLAMA_CONFIG},
                          headers={'Content-Type': 'application/json'},
                          timeout = 100)
        if response.status_code != 200:
            return None
        my_label.config(text=response.json()["response"].strip())
        return True

# clear function
def clear():
    my_text.delete(1.0, END)

# Grab the text from the text box
def get_text():
    my_label.config(text=my_text.get(1.0, END))

def define_prompt():
    input_prompt = my_prompt.get(1.0, END)
    return input_prompt

def clear_prompt():
    input_prompt = None
    my_prompt.delete(1.0, END)
    return input_prompt

my_prompt = Text(root, width = 60, height = 10)
my_prompt.pack(pady=20)

second_button_frame = Frame(root)
second_button_frame.pack()

my_text = Text(root, width = 100, height = 30)
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text ="Clear Text", command=clear)
clear_button.grid(row=0, column=0)

get_response_button = Button(button_frame, text="Get Response", command=run(input_prompt))
get_response_button.grid(row=0, column=1, padx=20)

input_prompt_button = Button(second_button_frame, text="Input Prompt", command=define_prompt)
input_prompt_button.grid(row=0, column=0)

clear_prompt_button = Button(second_button_frame, text="Clear Prompt", command=clear_prompt)
clear_prompt_button.grid(row=0, column=1, padx=20)

my_label = Label(root, text='')
my_label.pack(pady=20)

root.mainloop()