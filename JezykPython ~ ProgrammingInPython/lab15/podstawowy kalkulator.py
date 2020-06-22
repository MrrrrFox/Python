#!/usr/bin/env python3

from tkinter import *
from PIL import Image
import matplotlib.pyplot as plt
import tkinter.font

entryCol='#000000'
bgCol="#ffffff"


########################################################################

def onclick1():
    entry.insert(END, "1")
def onclick2():
    entry.insert(END, "2")
def onclick3():
    entry.insert(END, "3")

def onclickAdd():
    entry.insert(END, "+")
def onclickSub():
    entry.insert(END, "-")
def onclickEq():
    wart=eval(entry.get())
    entry.delete(0,END)
    entry.insert(0, str(wart))

def onclickRysuj():
    try:
        Image.open('wykr.png').save('wykr.gif')
        foto=PhotoImage(file="wykr.gif")
        cv.create_image(0,0,anchor=NW,image=foto)
    except:
        pass

def cl():
    entry.delete(0,END)
    cv.delete('all')

def exit():
    plt.close()
    root.destroy()

########################################################################

root = Tk()
root.title('Kalkulator')
root.protocol("WM_DELETE_WINDOW", exit)
calcfont=tkinter.font.Font(font=("Courier", 10, "bold"))

########################################################################

entry = Entry(root)
entry.config(width=60, fg="white", bg=entryCol, font=calcfont)
entry.grid(row=1, column=0, columnspan=8, pady=10)

########################################################################

button = Button(root, text='1', command=onclick1, bg=bgCol, font=calcfont)
button.grid(row=2, column=0, sticky=EW)

button = Button(root, text='2', command=onclick2, bg=bgCol, font=calcfont)
button.grid(row=2, column=1, sticky=EW)

button = Button(root, text='3', command=onclick3, bg=bgCol, font=calcfont)
button.grid(row=2, column=2, sticky=EW)

button = Button(root, text='+', command=onclickAdd, bg=bgCol, font=calcfont)
button.grid(row=2, column=4, sticky=EW)

button = Button(root, text='-', command=onclickSub, bg=bgCol, font=calcfont)
button.grid(row=2, column=5, sticky=EW)

button = Button(root, text='=', command=onclickEq, bg=bgCol, font=calcfont)
button.grid(row=2, column=6, sticky=EW)


button = Button(root, text='Rysuj', command=onclickRysuj, bg=bgCol, font=calcfont)
button.grid(row=6, column=2, sticky=EW)

button = Button(root, text='exit', command=exit, bg=bgCol, font=calcfont)
button.grid(row=5, column=5, sticky=EW)

button = Button(root, text='clear', command=cl, bg=bgCol, font=calcfont)
button.grid(row=5, column=4, sticky=EW)

#w = Label(root, text="label")
#w.grid(row=5, column=0)

########################################################################

cv = Canvas(root, width=400, height=300)
cv["background"]="white"
cv["borderwidth"]=0
cv.config()
cv.grid(row=10, column=0, columnspan=9)

########################################################################

root.mainloop()
