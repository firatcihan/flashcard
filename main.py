from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}
data = None
############# WORD PİCKİNG  #############
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") 

def button_command():
    canvas.itemconfig(foto, image=image_front)
    global current_card, timer
    win.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(text1, text=current_card["French"])
    timer = win.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(text1, text=current_card["English"])
    canvas.itemconfig(foto, image=image_back)


def is_known():
    to_learn.remove(current_card)
    dataframe = None
    dataframe = pandas.DataFrame(to_learn)
    dataframe.to_csv("data/words_to_learn.csv", index=False)
    button_command()


############# USER INTERFACE #############
win = Tk()
win.title("Flash card")
win.config(bg=BACKGROUND_COLOR,pady=50,padx=50) 
timer = win.after(3000, func=flip_card)


image_back = PhotoImage(file="images/back.png")
image_front = PhotoImage(file="images/front.png")
image_tik = PhotoImage(file="images/right.png")
image_carpi = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800,height=526)
foto = canvas.create_image(400, 263, image=image_front)
title = canvas.create_text(400,150, text="", font=("Ariel", 40, "italic"))
text1 = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0,columnspan=2,pady=15)

tikbutton = Button(image=image_tik, highlightthickness=0,command=is_known)
tikbutton.grid(row=1,column=1)

carpibutton = Button(image=image_carpi, highlightthickness=0, command=button_command)
carpibutton.grid(row=1,column=0)

button_command()

win.mainloop()
