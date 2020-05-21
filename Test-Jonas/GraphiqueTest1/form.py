from tkinter import *
from tkinter import filedialog
from injection import *
class Form(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)

    def close(self):
        bouton = Button(self, text="Close", command=self.quit)
        bouton.pack()

    def infect(self,entries):
        # period rate:
        pathToExe = entries['Path to the exe'].get()
        print('Path to the exe', pathToExe)

        pathToBadExe = entries['Path to the infected exe'].get()
        print('Path to the infected exe', pathToBadExe)

        sectionName = entries['Name of the section'].get()
        print('Name of the section', sectionName)

        inject = Injection(pathToExe,pathToBadExe,sectionName)
        inject.infect()

    def browseButton(self):
        file = filedialog.askopenfile(mode='rb', title='Browse a file',filetypes =[('Exe files', '*.exe')])
        if file != None:
            data = file.read()
            print(data)
            file.close()
        print(file)




    def makeform(self,fields):
        entries = {}
        for field in fields:
            row = Frame(self)
            lab = Label(row, width=22, text=field + ": ", anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
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

    def inputFile(self, inputVar):
        label = Label(self, text=inputVar)
        label.pack()
        btn = Button(text='Browse a file', command=lambda: Form.browseButton(self))
        btn.pack(side=RIGHT, expand=YES)
        entree = Entry(self, width=30)
        entree.pack()
        return entree

    def genInput(self):

        return entries
