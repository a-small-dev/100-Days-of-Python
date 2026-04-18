from tkinter import Canvas
import pandas as pd
import textwrap, random, tkinter as tk

BACKGROUND_COLOR = "#1E1E2F"
CANVAS_COLOR = "#2B2D42"
TEXT_COLOR = "#EDF2F4"
is_on = True

def get_term():
    keys = []
    for term in flash_words.keys():
        keys.append(term)

    return random.choice(keys)

def get_definition(term):
    return textwrap.fill(flash_words[term], width=40)

def next_card():
    global key
    key = get_term()
    term_label["text"] = get_definition(key)

def dont_remember():
    global key
    term_label["text"] = key
    window.after(2000, next_card)

def remembered():
    global key
    if len(flash_words) < 1:
        term_label["text"] = "Congratulations, you remembered all of the terms!"
        return
    term_label["text"] = key
    flash_words.pop(key)
    window.after(2000, next_card)

flash_data = pd.read_csv("top_60_cs_terms.csv")
flash_words = dict(zip(flash_data["Term"], flash_data["Definition"]))

#------ UI -----------------------------------#
window = tk.Tk()
window.title("Flashcards - Python/Computer Science")
window.configure(background=BACKGROUND_COLOR)
window.minsize(800, 700)

key = get_term()
definition = get_definition(key)

for i in range(10):
    window.grid_rowconfigure(i,weight=1, uniform="row")
    window.grid_columnconfigure(i,weight=1, uniform="col")

Canvas = Canvas(width=600, height=350, bg=CANVAS_COLOR, highlightthickness=2, highlightbackground="black")
Canvas.grid(row=3, column=1, pady=40, columnspan=8, rowspan=5)

flash_card_label = tk.Label(text="Flash Cards", fg=TEXT_COLOR, bg=BACKGROUND_COLOR, font=("Arial", 30))
flash_card_label.grid(row = 1, column = 1, pady = 10, columnspan = 8, rowspan = 2)

term_label = tk.Label(text=definition, fg=TEXT_COLOR, bg=CANVAS_COLOR, font=("Arial", 20))
term_label.grid(row=4, column=3, columnspan=4, rowspan=2)

wrong_button = tk.Button(width=4, height=2, text="X", fg="white", bg="#D90429", activebackground="#EF233C", font=("Arial", 14), command=lambda: dont_remember())
wrong_button.grid(row = 8, column = 3, rowspan = 2)

right_button = tk.Button(width=4, height=2, text="Y", fg="white", bg="#2EC4B6", activebackground="#38D9A9", font=("Arial", 14), command=lambda: remembered())
right_button.grid(row = 8, column = 6, rowspan = 2)

window.mainloop()

