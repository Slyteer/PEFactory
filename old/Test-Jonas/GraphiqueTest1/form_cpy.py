from tkinter import *
from tkinter import filedialog
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

    def browseButton(self):
        file = filedialog.askopenfile(mode='rb', title='Browse a file',filetypes =[('Exe files', '*.exe')])
        if file != None:
            data = file.read()
            print(data)
            file.close()


    def makeform(self, fields):
        entries = {}
        i=0
        for field in fields:
            row = Frame(self)
            lab = Label(row, width=22, text=field + " : ", anchor='w')
            ent = Entry(row)
            if (i<=1):
                btn = Button(text='Browse a file', command=lambda: Form.browseButton(self))
                btn.pack(side=RIGHT, expand=YES)
            row.pack(side=TOP, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries[field] = ent
            i +=1
        return entries


    def input(self, inputVar):
        label = Label(self, text=inputVar)
        label.pack()

        entree = Entry(self, width=30)
        entree.pack()
        return entree




    def genInput(self):

        return entries
