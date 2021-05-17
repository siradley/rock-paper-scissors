#import libraries
from tkinter import *
import random

#creating window bar
root = Tk() #initialized tkinter to create window
root.geometry('400x400') #sets width and height of the window
root.resizable(0, 0) #fix the size of the window
root.title('Rock, Paper, Scissors') #title of the window
root.config(bg = 'DodgerBlue2') #color of the background

#heading
Label(root, text = 'Rock, Paper, Scissors', font='Helvetica 20 bold', bg = 'DodgerBlue2').pack()

#label = to display text user cant modify
#root = name of our window
#text = display on the label as the title of that label
#font = which form the text is written
#pack = organized widget in form of block

#user choice
#user_take = string type variable that stores the choice that the user enters
user_take = StringVar()
Label(root, text = 'Choose one: rock, paper, scissors', font='Helvetica 15 bold', bg = 'DodgerBlue2').place(x = 35, y = 50)
#place() = place widgets at specific position
#Entry() = widget used when wanted to create an input text field
Entry(root, font = 'Helvetica 15', textvariable = user_take, bg = 'antiquewhite2').place(x = 90, y = 130)

#computer choice
comp_pick = random.randint(1, 3)
if comp_pick == 1:
    comp_pick = 'rock'
elif comp_pick == 2:
    comp_pick = 'paper'
else:
    comp_pick = 'scissors'

#random.randint() = randomly take any number from given number ( 1 to 3)

#Function to start game
Result = StringVar()

def play():
    user_pick = user_take.get()
    if user_pick == comp_pick:
        Result.set('tie, you both select same')
    elif user_pick == 'rock' and comp_pick == 'paper':
        Result.set('you lost, computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        Result.set('you win, computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        Result.set('you lost, computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        Result.set('you win, computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        Result.set('you, lost, computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        Result.set('you win, computer select paper')
    else:
        Result.set('invalid: choose any one -- rock, paper, scissors')

#Function to reset
#user_take = string type variable that stores the choice that user enters

def Reset():
    Result.set("")
    user_take.set("")

#function to exit
def Exit():
    root.destroy() #quit the game by stopping the mainloop()

#Define buttons
Entry(root, font = 'Helvetica 10 bold', textvariable = Result, bg = 'antiquewhite2', width = 50,).place(x = 25, y = 250)

Button(root, font = 'Helvetica 13 bold', text = 'Play', padx = 7, bg = 'seashell4', command = play).place(x = 165, y = 190)

Button(root, font = 'Helvetica 13 bold', text = 'Reset', padx = 5, bg = 'seashell4', command = Reset).place(x = 70, y = 310)
Button(root, font = 'Helvetica 13 bold', text = 'Exit', padx = 5, bg = 'seashell4', command = Exit).place(x = 255, y = 310)

#button() - used when we want to display a button
#command - called specific function when the button will be clicked
#root.mainloop() - method executes when we run our program

root.mainloop()