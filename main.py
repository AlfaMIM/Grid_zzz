from tkinter import *
from tkinter import scrolledtext
from PIL import Image, ImageTk

win = Tk()
win.title("Privet")
win.geometry('600x600')

def control():
    accept()
    picture()

def accept():
    show.config(text=spisok.get(ANCHOR))
    print(spisok.get(ANCHOR))
    if spisok.get(ANCHOR) == 'Овен':
        txt.delete(1.0, END)
        f = open('oven.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Телец':
        txt.delete(1.0, END)
        f = open('telec.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Близнецы':
        txt.delete(1.0, END)
        f = open('blizneci.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Рак':
        txt.delete(1.0, END)
        f = open('rak.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Лев':
        txt.delete(1.0, END)
        f = open('lev.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Дева':
        txt.delete(1.0, END)
        f = open('deva.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Весы':
        txt.delete(1.0, END)
        f = open('vesi.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Скорпион':
        txt.delete(1.0, END)
        f = open('skorpion.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Стрелец':
        txt.delete(1.0, END)
        f = open('strelec.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Козерог':
        txt.delete(1.0, END)
        f = open('kozerog.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Водолей':
        txt.delete(1.0, END)
        f = open('vodolei.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

    elif spisok.get(ANCHOR) == 'Рыбы':
        txt.delete(1.0, END)
        f = open('ribi.txt', encoding="utf-8-sig")
        s = f.read()
        txt.insert(INSERT, s)
        f.close()

def picture():
    global a
    a = ""
    show.config(text=spisok.get(ANCHOR))
    if spisok.get(ANCHOR) == "Овен":
        a = ImageTk.PhotoImage(Image.open('img/oven.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Телец':
        a = ImageTk.PhotoImage(Image.open('img/telec.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Близнецы':
        a = ImageTk.PhotoImage(Image.open('img/blizneci.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Рак':
        a = ImageTk.PhotoImage(Image.open('img/rak.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Лев':
        a = ImageTk.PhotoImage(Image.open('img/lev.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Дева':
        a = ImageTk.PhotoImage(Image.open('img/deva.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Весы':
        a = ImageTk.PhotoImage(Image.open('img/vesi.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Скорпион':
        a = ImageTk.PhotoImage(Image.open('img/skorpion.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Стрелец':
        a = ImageTk.PhotoImage(Image.open('img/strelec.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Козерог':
        a = ImageTk.PhotoImage(Image.open('img/kozerog.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Водолей':
        a = ImageTk.PhotoImage(Image.open('img/vodolei.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)
    elif spisok.get(ANCHOR) == 'Рыбы':
        a = ImageTk.PhotoImage(Image.open('img/ribi.gif'))
        b = Label(win, image=a, width=390, height=200, borderwidth=5)
        b.grid(column=2, row=1, padx=10)

spisok = Listbox(selectmode=SINGLE, width=10, height=12)
spisok.insert(0, 'Овен')
spisok.insert(1, 'Телец')
spisok.insert(2, 'Близнецы')
spisok.insert(3, 'Рак')
spisok.insert(4, 'Лев')
spisok.insert(5, 'Дева')
spisok.insert(6, 'Весы')
spisok.insert(7, 'Скорпион')
spisok.insert(8, 'Стрелец')
spisok.insert(9, 'Козерог')
spisok.insert(10, 'Водолей')
spisok.insert(11, 'Рыбы')
spisok.grid(column=0, row=0, padx=10)

Button(win, text='Подтвердить', command=control).grid(column=1, row=0)

txt = scrolledtext.ScrolledText(win, width=40, height=10, borderwidth=5)
txt.grid(column=2, row=0, padx=10)

show = Label(win)
win.mainloop()