import os
import tkinter.messagebox as tkmb

path = os.path.expanduser("~/Documents/Gestione alternanza/")
if not (os.path.exists(path)):
    os.makedirs(path)