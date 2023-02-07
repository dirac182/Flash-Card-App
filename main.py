from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#2C3333"
current_card = {}
to_learn = {}

#Read CSV Filez
try:
    csv_file = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    csv_file = pandas.read_csv("data/spanish_words.csv")

data = pandas.DataFrame(csv_file)
to_learn = data.to_dict(orient="records")
print(len(to_learn))

def word_gen():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    sp_word = current_card["spanish"]
    en_word = current_card["english"]
    flashcard.create_image(400, 263, image=card_front)
    flashcard.itemconfig(front_img,image=card_front)
    lang.config(text="Spanish",bg="white")
    word.config(text=sp_word,bg="white")
    flip_timer = window.after(3000, flip_card)

def flip_card():
    global current_card
    flashcard.create_image(400, 263, image=card_back)
    flashcard.itemconfig(back_img, image=card_back)
    lang.config(text="English",bg="#91c2af")
    word.config(text=current_card['english'],bg="#91c2af")

def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv",index=False)
    word_gen()

window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

flashcard = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
back_img = flashcard.create_image(400, 263, image=card_back)
front_img = flashcard.create_image(400,263,image=card_front)

flashcard.grid(column=0,row=0,columnspan=2)
#Language Label
lang = Label(flashcard,text="",font=("Ariel",40,"italic"),fg=BLACK,bg="white")
lang.grid(column=1,row=1)
flashcard.create_window(400,150,window=lang)
#Word Label
word = Label(flashcard,text="",font=("Ariel",60,"bold"),bg="white")
word.grid()
flashcard.create_window(400,263,window=word)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img,command=is_known)
right_button.grid(column=1,row=1,)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img,command=word_gen)
wrong_button.grid(column=0,row=1)

word_gen()

window.mainloop()
