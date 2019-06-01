import sqlite3 as sql
from src.Utils import *


def firstRun(cur):
    cur.executescript("""
    CREATE TABLE "classi" (
"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
"nome"	TEXT
);

CREATE TABLE "esperienze" (
"id"	INTEGER,
"denominazione"	TEXT,
"studente"	INTEGER,
"patto_formativo"	INTEGER,
"diario_bordo"	INTEGER,
"valutazione"	INTEGER
);

CREATE TABLE "studenti" (
"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
"nome"	TEXT,
"cognome"	TEXT,
"classe"	INTEGER
);
    """)

dbpath = path + "data.db"
dbo = sql.connect(dbpath, isolation_level=None)
cur = dbo.cursor()
cur.execute("SELECT * FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%';")
if len(cur.fetchall()) == 0:
    firstRun(cur)