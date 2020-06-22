#!/usr/bin/env python3
""""
1. Proszę zapisać wersję 0.0 (plik kal.py) kalkulatora i sprawdzić, że działa.
2. Proszę rozbudować kalkulator: wszystkie cyfry, działania: +, -, *, /, %, **, (, ), =.  (1p).
3. Proszę dodać możliwość rysowania wykresu funkcji korzystając z modułu matplotlib.pyplot;
użytkownik ma mieć możliwość określenia dziedziny (2p).
4. Proszę dodać możliwość całkowania metodą  quad z modułu scipy.integrate;
użytkownik ma mieć możliwość określenia granic całkowania (2p).
5. Proszę dodać możliwość znajdowania miejsc zerowych podanej funkcji metodą bisect z modułu scipy.optimize;
użytkownik określa przedział poszukiwania (2p).
6. Proszę dodać możliwość fitowania danych (dane testowe plik dane.txt) wczytywanych z pliku (np. numpy.loadtxt),
którego nazwę użytkownik podaje, z wykorzystaniem funkcji leastsq z modułu scipy.optimize.
Proszę narysować wykres obrazujący dane oraz dofitowaną funkcję z wykorzystaniem modułu matplotlib.pyplot (3p).
"""
from tkinter import *
from PIL import Image
from scipy import integrate
from scipy import optimize
import matplotlib.pyplot as plt
import tkinter.font
import numpy as np

entryCol = '#000000'
bgCol = "#ffffff"


########################################################################

def onclick1():
    entry.insert(END, "1")


def onclick2():
    entry.insert(END, "2")


def onclick3():
    entry.insert(END, "3")


def onclick4():
    entry.insert(END, "4")


def onclick5():
    entry.insert(END, "5")


def onclick6():
    entry.insert(END, "6")


def onclick7():
    entry.insert(END, "7")


def onclick8():
    entry.insert(END, "8")


def onclick9():
    entry.insert(END, "9")


def onclick0():
    entry.insert(END, "0")


def onclickAdd():
    entry.insert(END, "+")


def onclickSub():
    entry.insert(END, "-")


def onclickMulti():
    entry.insert(END, "*")


def onclickDiv():
    entry.insert(END, "/")


def onclickMod():
    entry.insert(END, "%")


def onclickPow():
    entry.insert(END, "**")


def onclickLeftBra():
    entry.insert(END, "(")


def onclickRightBra():
    entry.insert(END, ")")


def onclickEq():
    wart = eval(entry.get())
    entry.delete(0, END)
    entry.insert(0, str(wart))


def onclickRysuj():
    global foto
    try:
        plt.clf()
        x, y = ad3fun()
        plt.plot(x, y)
        plt.savefig('wykr.png', dpi=60)
        Image.open('wykr.png').save('wykr.gif')
        foto = PhotoImage(file="wykr.gif")
        cv.create_image(0, 0, anchor=NW, image=foto)
    except:
        pass


def onclickCalkuj():
    result = ad4fun()
    resultStr = 'Calka z: ' + entry.get() + ', to ' + str(result[0])
    entry.delete(0, END)
    entry.insert(0, resultStr)


def onclickBisect():
    try:
        result = ad5fun()
        resultStr = 'Znaleziono miejsce zerowe: ' + str(result)
        entry.delete(0, END)
        entry.insert(0, resultStr)
    except:
        entry.delete(0, END)
        entry.insert(0, 'Nie znaleziono miejsca zerowego')
        pass


def onclickFit():
    global foto
    try:
        funLine = lambda param, x: param[0]*x + param[1]
        plt.clf()
        x, y = ad6fun()
        plt.plot(x, y)
        plt.savefig('wykr.png', dpi=60)
        Image.open('wykr.png').save('wykr.gif')
        foto = PhotoImage(file="wykr.gif")
        cv.create_image(0, 0, anchor=NW, image=foto)
    except:
        print("brak pliku")



def cl():
    entry.delete(0, END)
    cv.delete('all')


def exit():
    plt.close()
    root.destroy()


########################################################################

root = Tk()
root.title('Kalkulator')
root.protocol("WM_DELETE_WINDOW", exit)
calcfont = tkinter.font.Font(font=("Courier", 10, "bold"))

########################################################################

entry = Entry(root)
entry.config(width=60, fg="white", bg=entryCol, font=calcfont)
entry.grid(row=1, column=0, columnspan=8, pady=10)

xMin = Entry(root)
xMin.grid(row=9, column=2, columnspan=2)
w1 = Label(root, text="x min")
w1.grid(row=8, column=2)

xMax = Entry(root)
xMax.grid(row=9, column=4, columnspan=2)
w2 = Label(root, text="x max")
w2.grid(row=8, column=4)

fitFile = Entry(root)
fitFile.grid(row=7, column=2, columnspan=2)
w3 = Label(root, text="plik do fitowania:")
w3.grid(row=7, column=1)
########################################################################

button = Button(root, text='1', command=onclick1, bg=bgCol, font=calcfont)
button.grid(row=2, column=0, sticky=EW)

button = Button(root, text='2', command=onclick2, bg=bgCol, font=calcfont)
button.grid(row=2, column=1, sticky=EW)

button = Button(root, text='3', command=onclick3, bg=bgCol, font=calcfont)
button.grid(row=2, column=2, sticky=EW)

button = Button(root, text='4', command=onclick4, bg=bgCol, font=calcfont)
button.grid(row=3, column=0, sticky=EW)

button = Button(root, text='5', command=onclick5, bg=bgCol, font=calcfont)
button.grid(row=3, column=1, sticky=EW)

button = Button(root, text='6', command=onclick6, bg=bgCol, font=calcfont)
button.grid(row=3, column=2, sticky=EW)

button = Button(root, text='7', command=onclick7, bg=bgCol, font=calcfont)
button.grid(row=4, column=0, sticky=EW)

button = Button(root, text='8', command=onclick8, bg=bgCol, font=calcfont)
button.grid(row=4, column=1, sticky=EW)

button = Button(root, text='9', command=onclick9, bg=bgCol, font=calcfont)
button.grid(row=4, column=2, sticky=EW)

button = Button(root, text='0', command=onclick0, bg=bgCol, font=calcfont)
button.grid(row=5, column=1, sticky=EW)

button = Button(root, text='+', command=onclickAdd, bg=bgCol, font=calcfont)
button.grid(row=2, column=4, sticky=EW)

button = Button(root, text='-', command=onclickSub, bg=bgCol, font=calcfont)
button.grid(row=2, column=5, sticky=EW)

button = Button(root, text='=', command=onclickEq, bg=bgCol, font=calcfont)
button.grid(row=2, column=6, sticky=EW)

button = Button(root, text='*', command=onclickMulti, bg=bgCol, font=calcfont)
button.grid(row=3, column=4, sticky=EW)

button = Button(root, text='/', command=onclickDiv, bg=bgCol, font=calcfont)
button.grid(row=3, column=5, sticky=EW)

button = Button(root, text='%', command=onclickMod, bg=bgCol, font=calcfont)
button.grid(row=3, column=6, sticky=EW)

button = Button(root, text='**', command=onclickPow, bg=bgCol, font=calcfont)
button.grid(row=4, column=4, sticky=EW)

button = Button(root, text='(', command=onclickLeftBra, bg=bgCol, font=calcfont)
button.grid(row=4, column=5, sticky=EW)

button = Button(root, text=')', command=onclickRightBra, bg=bgCol, font=calcfont)
button.grid(row=4, column=6, sticky=EW)

button = Button(root, text='Rysuj', command=onclickRysuj, bg=bgCol, font=calcfont)
button.grid(row=6, column=2, sticky=EW)

button = Button(root, text='Calkuj', command=onclickCalkuj, bg=bgCol, font=calcfont)
button.grid(row=6, column=3, sticky=EW)

button = Button(root, text='Bisekcja', command=onclickBisect, bg=bgCol, font=calcfont)
button.grid(row=6, column=4, sticky=EW)

button = Button(root, text='Fituj', command=onclickFit, bg=bgCol, font=calcfont)
button.grid(row=7, column=4, sticky=EW)

button = Button(root, text='exit', command=exit, bg=bgCol, font=calcfont)
button.grid(row=5, column=5, sticky=EW)

button = Button(root, text='clear', command=cl, bg=bgCol, font=calcfont)
button.grid(row=5, column=4, sticky=EW)

# w = Label(root, text="label")
# w.grid(row=5, column=0)

########################################################################

cv = Canvas(root, width=400, height=300)
cv["background"] = "white"
cv["borderwidth"] = 0
cv.config()
cv.grid(row=10, column=0, columnspan=9)


########################################################################

def ad3fun():
    N = 10 ** 5
    przedzial = [float(xMin.get()), float(xMax.get())]

    krok = (przedzial[1] - przedzial[0]) / N
    x_tab = []
    y_tab = []

    for i in range(N):
        x = przedzial[0] + i * krok
        x_tab.append(x)
        y_tab.append(eval(entry.get()))
    return x_tab, y_tab


def ad4fun():
    return integrate.quad(lambda x: eval(entry.get()), float(xMin.get()), float(xMax.get()))


def ad5fun():
    return optimize.bisect(lambda x: eval(entry.get()), float(xMin.get()), float(xMax.get()))

def ad6fun():
    data = np.loadtxt(fitFile.get()).tolist()
    x_tab = [data[i][0] for i in range(len(data))]
    y_tab = [data[i][1] for i in range(len(data))]
    return x_tab, y_tab


########################################################################

root.mainloop()
