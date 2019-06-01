from src.Window import *
import modules.Classi as Classi
import modules.Studenti as Studenti
import modules.Esperienze as Esperienze

w = Window()
ft = Frame(w)
ft.pack()
icon = PhotoImage(master=ft, file="assets/img/office-material.png")
icon_label = Label(ft, image=icon)
icon_label.grid(row=0, column=0)
title = Label(ft, text="Gestione alternanza", font=("Comic Sans MS", 20, "bold"))
title.grid(row=0, column=1)
fa = Frame(w)
fa.pack(pady=10)
icon_c = PhotoImage(master=fa, file="assets/img/blackboard.png")
bc = Button(fa, text="Classi", image=icon_c, compound=LEFT, command=Classi.list)
bc.grid(row=0, column=0, padx=10, pady=5)
icon_s = PhotoImage(master=fa, file="assets/img/student.png")
bs = Button(fa, text="Studenti", image=icon_s, compound=LEFT, command=Studenti.list)
bs.grid(row=0, column=1, padx=10, pady=5)
icon_e = PhotoImage(master=fa, file="assets/img/briefcase.png")
be = Button(fa, text="Esperienze", image=icon_e, compound=LEFT, command=Esperienze.lista)
be.grid(row=1, column=0, padx=10)
w.mainloop()
