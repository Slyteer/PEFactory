""" INTERFACE GRAPHIQUE DU LOGICIEL PEFACTORY
CREATED by Arthur_Jonas
"""

from tkinter import *
from form import *
from tkinter import filedialog


def form():

    window = Tk()
    window.title("PEFactory")
    window.iconbitmap("malware.ico")
    center_window(window)

    interface = Form(window)
    fields = ('Path to the exe', 'Path to the infected exe', 'Name of the section')

    entries = interface.makeform(fields)
    b1 = Button(interface, text='Inject',
                command=(lambda e=entries: interface.infect(e)))

    b1.pack()

    #btn = Button(text='Browse a file', command=lambda: Form.browseButton(interface))
    #btn.pack(side=RIGHT, expand=YES)

    interface.close()

    # PYTHON TU ES DU VOMIS DE CHAT QUAND JE LANCE UNE FONCTION PREND LES ARGUMENT LA PAS AVANT SALLE VACHE TU PU T MOCHE
    interface.mainloop()



def center_window(root,w=700, h=700):

    # get screen width and height
    width_screen = root.winfo_screenwidth()
    height_screen = root.winfo_screenheight()

    # On calcule la positon x et y pour placer la fenetre au centre
    x = (width_screen/2) - (w/2)
    y = (height_screen/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))


def browseButton(self):
    file = filedialog.askopenfile(mode='rb', title='Browse a file', filetypes=[('Exe files', '*.exe')])
    if file != None:
        data = file.read()
        file.close()
    print(file)

form()
