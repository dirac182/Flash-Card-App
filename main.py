from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#2C3333"

#Read CSV File
import pandas
import random
file = pandas.read_csv("data/spanish_words.csv")
data = pandas.DataFrame(file)
sp_words = data["spanish"].tolist()
random_word = random.choice(sp_words)



window = Tk()
window.title("Flash Cards")
#window.minsize(width=1000,height=750)
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flashcard = Canvas(height=526,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
card_bg = PhotoImage(file="images/card_front.png")
flashcard.create_image(400,263,image=card_bg)
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
right_button = Button(image=right_img)
right_button.grid(column=1,row=1,)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img)
wrong_button.grid(column=0,row=1)


















window.mainloop()
