from tkinter import *

class Window(Frame):
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)

        # On créer notre premier widget
        self.label = Label(self,text="Faites votre virus");
        self.label.pack()
        # entrée
        value = StringVar()
        value.set("texte par défaut")
        test = None
        entree = Entry(fenetre, textvariable=test, width=30)
        entree.pack()
        bouton = Button(fenetre, text="Fermer", command=fenetre.quit)
        bouton.pack()


