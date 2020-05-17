from tkinter import *
from injection import *
class Form(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        self.pathExe = None
        self.pathBadExe = None
        self.nameSec = None

    def close(self):
        bouton = Button(self, text="Close", command=self.quit)
        bouton.pack()

    def infect(self):
        bouton = Button(self, text="Infect", command=self.quit)
        bouton.pack()

    def makeform(self, fields):
        entries = {}
        for field in fields:
            row = Frame(self)
            lab = Label(row, width=22, text=field + ": ", anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries[field] = ent
        return entries


    def input(self, inputVar):
        label = Label(self, text=inputVar)
        label.pack()

        entree = Entry(self, width=30)
        entree.pack()
        return entree

    def genInput(self):

        return entries
