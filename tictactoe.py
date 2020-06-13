import tkinter as tk
from tkinter import *
from functools import partial

win = tk.Tk()

win.title("tictactoe")

win.resizable(True, True)

text1 = " "
text2 = " "
text3 = " "
text4 = " "
text5 = " "
text6 = " "
text7 = " "
text8 = " "
text9 = " "

isXturn = True
def onclick(button):
    global isXturn
    if isXturn == True:
        button.config(text="X")
        button.config(relief=SUNKEN)
        button.config(state=DISABLED)
        isXturn = False
        winState("X")
    else:
        button.config(text="O")
        button.config(relief=SUNKEN)
        button.config(state=DISABLED)
        isXturn = True
        winState("O")

def restartGame():
    global button1
    button1.config(relief=RAISED, text=" ", state=NORMAL)
    global button2
    button2.config(relief=RAISED, text=" ", state=NORMAL)
    global button3
    button3.config(relief=RAISED, text=" ", state=NORMAL)
    global button4
    button4.config(relief=RAISED, text=" ", state=NORMAL)
    global button5
    button5.config(relief=RAISED, text=" ", state=NORMAL)
    global button6
    button6.config(relief=RAISED, text=" ", state=NORMAL)
    global button7
    button7.config(relief=RAISED, text=" ", state=NORMAL)
    global button8
    button8.config(relief=RAISED, text=" ", state=NORMAL)
    global button9
    button9.config(relief=RAISED, text=" ", state=NORMAL)
    global isXturn
    isXturn = True
    global label1
    label1.config(text=" ")

def winState(x):
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9

    if (button1['text'] == x) & (button2['text'] == x) & (button3['text'] == x):
        winLabel(x)
        disableButtons()
        return
    if (button4['text'] == x) & (button5['text'] == x) & (button6['text'] == x):
        winLabel(x)
        disableButtons()
        return
    if (button7['text'] == x) & (button8['text'] == x) & (button9['text'] == x):
        winLabel(x)
        disableButtons()
        return
    if (button1['text'] == x) & (button4['text'] == x) & (button7['text'] == x):
        winLabel(x)
        disableButtons()
        return
    if (button2['text'] == x) & (button5['text'] == x) & (button8['text'] == x):
        winLabel(x)
        disableButtons()
        return
    if (button3['text'] == x) & (button6['text'] == x) & (button9['text'] == x):
        winLabel(x)
        disableButtons()
        return
    if (button1['text'] == x) & (button5['text'] == x) & (button9['text'] == x):
        winLabel(x)
        disableButtons()
        return
    if (button3['text'] == x) & (button5['text'] == x) & (button7['text'] == x):
        winLabel(x)
        disableButtons()
        return

def winLabel(x):
    if x == "X":
        label1.config(text='X wins!')
    else:
        label1.config(text='O wins!')

def disableButtons():
    global button1
    global button2
    global button3
    global button4
    global button5
    global button6
    global button7
    global button8
    global button9
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)

label1 = tk.Label(win, text='')
label1.grid(row=0, column=3, padx=10)

button1 = tk.Button(win, text=" ", relief=RAISED, height=3, width=4)
button1.grid(row=0, column=0, ipadx=15, ipady=10)
button1.config(command=partial(onclick, button1))
button2 = tk.Button(win, text=" ", relief=RAISED, height=3, width=4)
button2.grid(row=0, column=1, ipadx=15, ipady=10)
button2.config(command=partial(onclick, button2))
button3 = tk.Button(win, text=" ", relief=RAISED, height=3, width=4)
button3.grid(row=0, column=2, ipadx=15, ipady=10)
button3.config(command=partial(onclick, button3))

button4 = tk.Button(win, text=" ", relief=RAISED, height=3, width=4)
button4.grid(row=1, column=0, ipadx=15, ipady=10)
button4.config(command=partial(onclick, button4))
button5 = tk.Button(win, text=" ", relief=RAISED, height=3, width=4)
button5.grid(row=1, column=1, ipadx=15, ipady=10)
button5.config(command=partial(onclick, button5))
button6 = tk.Button(win, text=" ", relief=RAISED, height=3, width=4)
button6.grid(row=1, column=2, ipadx=15, ipady=10)
button6.config(command=partial(onclick, button6))

button7 = tk.Button(win, text=" ", relief=RAISED, height=3, width=4)
button7.grid(row=2, column=0, ipadx=15, ipady=10)
button7.config(command=partial(onclick, button7))
button8 = tk.Button(win, text=" ", relief=RAISED, height=3, width=4)
button8.grid(row=2, column=1, ipadx=15, ipady=10)
button8.config(command=partial(onclick, button8))
button9 = tk.Button(win, text=" ", relief=RAISED, height=3, width=4)
button9.grid(row=2, column=2, ipadx=15, ipady=10)
button9.config(command=partial(onclick, button9))

button10 = tk.Button(win, text="Restart", relief=RAISED)
button10.grid(row=1, column=3, padx=10)
button10.config(command=restartGame)
win.mainloop()
