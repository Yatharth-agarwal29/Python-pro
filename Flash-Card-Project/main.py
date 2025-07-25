BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import math , pandas
import random
#---------------------------------------------------------------------------------------------------------
timer = None
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

def flip_card():
    global current_card
    canvas.itemconfig(card , image=card_back_img )
    canvas.itemconfig(card_title, text = "English",fill="white")
    canvas.itemconfig(card_word, text = current_card["English"],fill="white")
    window.after_cancel(id=timer)

def new_card():
    global current_card , timer
    window.after_cancel(timer)
    current_card= random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French" , fill="black")
    canvas.itemconfig(card_word, text = current_card["French"] , fill="black")  
    canvas.itemconfig(card , image=card_front_img )
    timer = window.after(3000 ,func= flip_card)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card() 
#---------------------------------------------------------------------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000 ,func= flip_card)
#------------------------------------------------------------------------------------------------
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
yes_img = PhotoImage(file="images/right.png")
no_img = PhotoImage(file="images/wrong.png")
#-------------------------------------------------------------------------------------------------
canvas=Canvas(width=800,height=526 , highlightthickness= 0 , bg= BACKGROUND_COLOR )
card=canvas.create_image(400,263,image=card_front_img )
card_title=canvas.create_text(400,150 , text="French to",font=("Ariel" , 40, "italic"))
card_word = canvas.create_text(400,263,text="English words",font=("Ariel" , 40, "bold"))
canvas.grid(row=0,column=0 , columnspan= 2)
# ----------------------------------------------------------yes_img)
button_right=Button(highlightthickness= 0 , bg= BACKGROUND_COLOR,  image=yes_img , command= is_known )
button_right.grid(row=1,column=0 ,)
#-----------------------------------------------------------------------------------------
button_cross=Button(highlightthickness= 0 , bg= BACKGROUND_COLOR , image=no_img , command= new_card )
button_cross.grid(row=1,column=1 )



new_card()
window.mainloop()
