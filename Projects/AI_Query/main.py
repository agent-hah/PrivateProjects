from tkinter import *

root = Tk()
root.title('Ollama_GPT')
root.geometry("800x600")

# clear function
def clear():
    my_text.delete(1.0, END)
    
my_text = Text(root, width = 100, height = 30)
my_text.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

clear_button = Button(button_frame, text ="Clear Screen", command=clear)
clear_button.grid(row=0, column=0)

root.mainloop()