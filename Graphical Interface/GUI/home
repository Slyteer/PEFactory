""" INTERFACE GRAPHIQUE DU LOGICIEL PEFACTORY
CREATED by Arthur_
"""

from tkinter import *
from window import *


def home_page():

    window = Tk()
    window.title("PEFactory")
    window.iconbitmap("../../img/malware.ico")
    center_window(window)

    interface = Window(window)



    interface.mainloop()
    interface.destroy()




def center_window(root,w=700, h=700):

    # get screen width and height
    width_screen = root.winfo_screenwidth()
    height_screen = root.winfo_screenheight()

    # On calcule la positon x et y pour placer la fenetre au centre
    x = (width_screen/2) - (w/2)
    y = (height_screen/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

home_page()
