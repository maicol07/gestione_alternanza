from tkinter import *
from tkinter.ttk import *


class Window(Tk):
    def __init__(self, bg="white", icon="assets/office-material.ico", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=bg)
        self.iconbitmap(icon)
        self.title("Gestione alternanza")
        # Stili TTK
        global s
        s = Style()
        s.configure("TLabel", background="white")
        s.configure("TFrame", background="white")
        s.configure("TLabelframe", background="white")
        s.configure("TLabelframe.Label", background="white")


class Toplevel(Toplevel):
    def __init__(self, title="Gestione alternanza", bg="white", icon="assets/office-material.ico", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configure(background=bg)
        self.iconbitmap(icon)
        self.title("Gestione alternanza | " + title)