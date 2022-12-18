import sqlite3
from tkinter import Tk

gr = ["2022-12-01", "2022-12-02", "2022-12-03", "2022-12-04", "2022-12-05", "2022-12-06", "2022-12-07", "2022-12-08", "2022-12-09", "2022-12-10", "2022-12-11", "2022-12-12", "2022-12-13", "2022-12-14", "2022-12-15", "2022-12-16", "2022-12-17", "2022-12-18", "2022-12-19", "2022-12-20", "2022-12-21", "2022-12-22", "2022-12-23", "2022-12-24", "2022-12-25", "2022-12-26", "2022-12-27", "2022-12-28", "2022-12-29", "2022-12-30", "2022-12-31", ]

"""root = Tk()
root.title('Kalendarz')
root.geometry("600x400")
root.mainloop()"""

db = sqlite3.connect(r"C:\Users\Coding\Desktop\Coding\FinAnas\\simple.db")
cursor = db.cursor()
cursor.execute(
'''CREATE TABLE IF NOT EXISTS kalendarz(
        ID	    INTEGER NOT NULL UNIQUE,
        Data    DATE NOT NULL, 
        Data_ID STRING NOT NULL,
        Godziny	INTEGER NOT NULL,
        Stawka	INTEGER NOT NULL,
        Wartość INTEGER,
        PRIMARY KEY("ID" AUTOINCREMENT)
    );''')

db.commit
db.close()


while True:

    db = sqlite3.connect("simple.db")
    cursor = db.cursor()

    
    
    choice = input("Wybierz opcje: ")

    match choice:
        case  '1':

            
            dt = input(" Podaj datę: ")
            dt_id = input("Podaj data_id: ")
            rg = int(input('Podaj ilość godzin: '))
            st = int(input("Podaj stawkę: "))
            wr = rg * st



            db.execute('INSERT INTO kalendarz (Data, Data_ID, Godziny, Stawka, Wartość) VALUES (?, ?, ?, ?, ?);',(dt, dt_id, rg, st, wr))   
            db.commit()
            db.close()

        case '2':

            cursor.execute('SELECT * FROM kalendarz GROUP BY Data')
            
            rows = cursor.fetchall()
            
            for x in rows:
                print("+" +'-' * 17 + "+")
                print( "|Data: ",    x[1])
                print( "|Data_ID: ", x[2])
                print( "|Godziny: ", x[3])
                print( "|Stawka: ",  x[4])
                print( "|Wartość: ", x[5])
                print("+" +'-' * 17 + "+")

            cursor.close()


        case '0':
            break







