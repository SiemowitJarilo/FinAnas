import sqlite3


def db_create_kpir():
    db = sqlite3.connect("simple.db")
    cursor = db.cursor()
    cursor.execute(
    '''CREATE TABLE IF NOT EXISTS koszty(
            ID	    INTEGER NOT NULL UNIQUE PRIMARY KEY  AUTOINCREMENT,
            Data    DATE NOT NULL, 
            Data_ID STRING NOT NULL,
            Ilość	INTEGER NOT NULL,
            Netto	FLOAT NOT NULL,
            P_VAT   FLOAT NOT NULL,
            W_VAT   FLOAT NOT NULL,
            Brutto  FLOAT NOT NULL
        );''')

    db.commit

def db_create_kalendarz():
    db = sqlite3.connect("simple.db")
    cursor = db.cursor()
    cursor.execute(
    '''CREATE TABLE IF NOT EXISTS kalendarz(
            ID	    INTEGER NOT NULL UNIQUE,
            Data    DATE NOT NULL, 
            Data_ID STRING NOT NULL,
            Godziny	INTEGER NOT NULL,
            Stawka	INTEGER NOT NULL,
            Wartość FLOAT NOT NULL,
            S_VAT   FLOAT NOT NULL,
            W_VAT   FLOAT NOT NULL,
            W_Brutto FLOAT NOT NULL,
            PRIMARY KEY("ID" AUTOINCREMENT)
        );''')

    db.commit