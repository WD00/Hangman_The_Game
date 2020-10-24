from tkinter import *
from string import ascii_uppercase
from tkinter import messagebox
import random


window = Tk()
window.title("Hangman The Programmer")

word_list = ["R", "KOTLIN", "PYTHON", "C", "JAVA", "RUBY", "PASCAL", "ADA", "FORTRAN",
                    "JAVASCRIPT", "SWIFT", "RUST", "GO", "LUA"]

photos = [PhotoImage(file="HM_img/0.png"),PhotoImage(file="HM_img/1.png"),PhotoImage(file="HM_img/2.png"),
          PhotoImage(file="HM_img/3.png"),PhotoImage(file="HM_img/4.png"),PhotoImage(file="HM_img/5.png"),
          PhotoImage(file="HM_img/6.png"),PhotoImage(file="HM_img/7.png"),PhotoImage(file="HM_img/8.png"),
          PhotoImage(file="HM_img/9.png"),PhotoImage(file="HM_img/10.png"),PhotoImage(file="HM_img/11.png")]

def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    numberOfGuesses = 0
    imgLabel.config(image = photos[0])
    the_word = random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(" ".join("_"*len(the_word)))

def guess(letter):
    global numberOfGuesses
    if numberOfGuesses<11:
        txt = list(the_word_withSpaces)
        guessed = list(lblWord.get())
        if the_word_withSpaces.count(letter)>0:
            for c in range (len(txt)):
                if txt[c]==letter:
                    guessed[c]=letter
                lblWord.set("".join(guessed))
                if lblWord.get()==the_word_withSpaces:
                    messagebox.showinfo("Hangman The Programmer", "Congratulations! You win!")
                    newGame()
        else:
            numberOfGuesses+=1
            imgLabel.config(image = photos[numberOfGuesses])
            if numberOfGuesses == 11:
                messagebox.showwarning("Hangman The Programmer", "Unfortunately, that was not correct. Game over!")

imgLabel = Label(window)
imgLabel.grid(row = 0, column = 0, columnspan = 3, padx = 10, pady = 40)
imgLabel.config(image = photos[0])

lblWord = StringVar()
Label(window, textvariable = lblWord, font = ("Consolas 24 bold")).grid(row = 0, column= 3, columnspan = 6, padx = 10)

n = 0
for c in ascii_uppercase:
    Button(window, text = c, command = lambda b = c: guess(b), font = ("Helvetica 18"), width = 4).grid(row =1 + n // 9, column=n % 9)
    n+=1

Button(window, text = "Start \n Over", command = lambda:newGame(), font = "Helvetica 13", width = 4).grid(row=1+n//9, column=n%9, sticky = "NSWE")

newGame()
window.mainloop()