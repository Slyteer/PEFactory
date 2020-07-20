from tkinter import *

class Window(Frame):
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)

        # On créer notre premier widget
        self.label = Label(self,text="Jonas est une pute");
        self.label.pack()


