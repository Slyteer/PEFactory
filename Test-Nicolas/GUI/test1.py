from tkinter import *

window = Tk()

window.title("PEFactory")

window.geometry('350x200')

lbl = Label(window, text="PEFactory")

lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=1, row=2)

txt.focus()

txt = Entry(window,width=10)

txt.grid(column=1, row=4)

txt = Entry(window,width=10)

txt.grid(column=1, row=6)

def clicked():

    lbl.configure(text="Infecting...")

btn = Button(window, text="Infect", command=clicked)

btn.grid(column=2, row=2)

btn = Button(window, text="Infect", command=clicked)

btn.grid(column=2, row=4)

btn = Button(window, text="Infect", command=clicked)

btn.grid(column=2, row=6)

window.mainloop()

