from src.Database import *
from src.Window import *
from src.EditableTreeview import *


def on_closing(w, t):
    if tkmb.askyesno("Conferma salvataggio", "Desideri salvare prima di chiudere?"):
        saveData(t)
    w.destroy()


def lista():
    w = Toplevel(title="Esperienze")
    t = Tk_Table(w, columns=["ID", "denominazione", "studente", "patto formativo", "diario di bordo", "valutazione"], row_numbers=True, editable=True, stripped_rows=("white", "#e3e3e3"))
    t.pack(expand=True, fill=BOTH)
    getEsperienze(t)
    fb = Labelframe(w, text="Azioni")
    fb.pack()
    icon_add = PhotoImage(master=w, file="assets/img/add.png")
    icon_delete = PhotoImage(master=w, file="assets/img/clear.png")
    icon_save = PhotoImage(master=w, file="assets/img/save.png")
    b_add = Button(fb, text="Aggiungi una riga", image=icon_add, compound=LEFT, command=lambda: addRiga(t))
    b_add.grid(row=0, column=0, pady=10, padx=5)
    b_delete = Button(fb, text="Elimina le righe selezionate", image=icon_delete, compound=LEFT,  command=lambda: delete_rows(w, t))
    b_delete.grid(row=0, column=1, pady=10, padx=5)
    b_save = Button(fb, text="Salva", image=icon_save, compound=LEFT,  command=lambda: saveData(t))
    b_save.grid(row=0, column=2, pady=10, padx=5)
    w.protocol("WM_DELETE_WINDOW", lambda: on_closing(w, t))
    w.mainloop()
    cur.close()
    dbo.close()


def addRiga(t):
    try:
        id = t.table_data
        new_id = 0
        for i in id:
            if i[0] > new_id:
                new_id = i[0]
        t.insert_row([new_id + 1, "", "", "", "", ""])
    except IndexError:
        t.insert_row([1, "", "", "", "", ""])


def delete_rows(master, t):
    if tkmb.askyesno(master=master, title="Conferma eliminazione", message="Sei sicuro di eliminare le righe selezionate?"):
        for i in t.selected_rows:
            cur.execute("DELETE FROM esperienze WHERE id=?", (i[0],))
        t.delete_all_selected_rows()


def getEsperienze(t):
    cur.execute("SELECT esperienze.id, esperienze.denominazione, studenti.cognome, esperienze.patto_formativo,"
                "esperienze.diario_bordo, esperienze.valutazione FROM esperienze INNER JOIN studenti ON esperienze.studente = studenti.id")
    rows = cur.fetchall()
    for row in rows:
        row = list(row)
        for i in [3, 4, 5]:
            if row[i] is 1:
                row[i] = "S"
            else:
                row[i] = "N"
        t.insert_row([row[0], row[1], row[2], row[3], row[4], row[5]])


def saveData(t):
    rows = list(t.table_data)
    for data in rows:
        cur.execute("SELECT id FROM esperienze")
        id_list = ()
        for i in cur.fetchall():
            id_list += (i[0],)
        cur.execute("SELECT id FROM studenti WHERE cognome=?", (data[2],))
        studente = cur.fetchone()
        if type(studente) is not tuple:
            tkmb.showerror("Nessuno studente trovato", message="Non è stato trovato nessuno studente registrato con quel nome. Si prega di crearlo prima di inserirlo nell'esperienza")
            continue
        for i in [2, 3, 4]:
            if data[i] == "S":
                data[i] = 1
            else:
                data[i] = 0
        if data[0] in id_list:
            cur.execute("UPDATE esperienze SET denominazione=?, studente=?, patto_formativo=?, diario_bordo=?,"
                        "valutazione=? WHERE id=?", (data[1], data[2], studente[0], data[3], data[4], data[0]))
        else:
            cur.execute("INSERT INTO esperienze (id, denominazione, studente, patto_formativo, diario_bordo,"
                        "valutazione) VALUES (?, ?, ?, ?, ?, ?)", (data[0], data[1], studente[0], data[2], data[3], data[4]))
