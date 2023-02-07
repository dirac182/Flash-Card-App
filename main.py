from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#2C3333"

#Read CSV Filez

file = pandas.read_csv("data/spanish_words.csv")
data = pandas.DataFrame(file)
data_dict = dict(zip(data.spanish,data.english))
sp_words = data["spanish"].tolist()

try:
    with open(file="words_to_learn.csv",mode="r") as file:
        data = pandas.read_csv()

except FileNotFoundError:
    data.to_csv("words_to_learn.csv",index=False)



random_word = ""
translation = ""


def word_gen():
    global random_word
    global translation
    random_word = random.choice(sp_words)
    translation = data_dict[random_word]
    flashcard.create_image(400, 263, image=card_front)
    flashcard.itemconfig(front_img,image=card_front)
    lang.config(text="Spanish")
    word.config(text=random_word)
    window.after(3000, flip_card)

def flip_card():
    flashcard.create_image(400, 263, image=card_back)
    flashcard.itemconfig(back_img, image=card_back)
    lang.config(text="English")
    word.config(text=translation)

window = Tk()
window.title("Flash Cards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flashcard = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
back_img = flashcard.create_image(400, 263, image=card_back)
front_img = flashcard.create_image(400,263,image=card_front)

flashcard.grid(column=0,row=0,columnspan=2)
#Language Label
lang = Label(flashcard,text="Spanish",font=("Ariel",40,"italic"),fg=BLACK)
lang.grid(column=1,row=1)
flashcard.create_window(400,150,window=lang)
#Word Label
word = Label(flashcard,text="Word",font=("Ariel",60,"bold"))
word.grid()
flashcard.create_window(400,263,window=word)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img,command=word_gen)
right_button.grid(column=1,row=1,)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img,command=word_gen)
wrong_button.grid(column=0,row=1)


















window.mainloop()
