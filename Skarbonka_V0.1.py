import sqlite3 
from zondaRequest import zonda


# 1. 
# 2. 
# 3. 

def commitMe():
    db.commit()
    print("Dane dodano poprwanie")
    db.close()

db = sqlite3.connect("simple.db")
cursor = db.cursor()

cursor.execute('''

    CREATE TABLE IF NOT EXISTS inwestycje(
    ID          INTEGER     PRIMARY KEY     AUTOINCREMENT,
    NAZWA       STRING,
    WARTOŚĆ     INTEGER,
    KWOTA       INTEGER)
        ''')

cursor.execute('''

    CREATE TABLE IF NOT EXISTS fundusze(
    ID          INTEGER     PRIMARY KEY     AUTOINCREMENT,
    NAZWA       STRING,
    KWOTA       INTEGER,
    invest_ID   INTEGER,
    FOREIGN KEY(invest_ID) REFERENCES inwestycje(ID)
    );''')        
db.commit
db.close()


print("Skarbonka v0.1")
print("-" * 79)
db = sqlite3.connect("simple.db")
print()
print()
print()

while True:
    
    db = sqlite3.connect("simple.db")
    cursor = db.cursor()
    db.commit()


    
    choice = int(input("Wybierz opcje: "))
    
    if choice == 1: # Pokaz skarbonkę

### Problem: Brak sumowania "Kwota" z tabeli "fundusze"

        cursor.execute(''' SELECT 
                                inwestycje.ID,
                                inwestycje.NAZWA,
                                inwestycje.WARTOŚĆ,
                                inwestycje.KWOTA
                            FROM 
                                inwestycje
                                
                                                     
                          
    ''')

        rows = cursor.fetchall()
        
        for x in rows:
            print("-" * 79)
            print( "ID: ", x[0])
            print( "Nazwa: ", x[1])
            print( "WARTOŚĆ: ", x[2])
            print( "Kwota: ", x[3])
            print('-' * 79)

        cursor.close()
#
    if choice == 2: # Dodaj skarbonkę
            try:
        
            
                nazwa = input("Podaj nazwę skarbonki: ")
                wartość = int(input("Podaj kwotę skarbonki: "))
                kwota = int(input("Podaj kwotę pierwszej wpłaty: "))                
                
                cursor.execute(''' INSERT INTO 
                                        inwestycje
                                            (NAZWA,
                                            WARTOŚĆ,
                                            KWOTA) 
                                        VALUES (?, ?, ?);''', 
                                            (nazwa, wartość, kwota))
                                                                                
                commitMe()

            except sqlite3.Error as e:
                print("Error -> Coś poszło nie tak", e)

            finally:
                if (db) :
                    db.close()
                    print("Połączenie zamknięte")
                    print("-" * 79)
    
    if choice == 3: # Pokaż kwoty Skarbonek
        #db = sqlite3.connect("simple.db")
        #cursor = db.cursor()
      
### Problem: Sumuje wszystkie "Kwoty" dla każdej "Nazwy/ID"


        cursor.execute(''' SELECT 
                                invest_ID,
                                NAZWA, 
                                KWOTA
                            FROM 
                                fundusze
                            GROUP BY NAZWA
        ''')

        rows = cursor.fetchall()

        

        for x in rows:
            print("-" * 79)
            print( "ID: ", x[0])
            print( "Nazwa: ", x[1])
            print( "Kwota: ", x[2])
            print('-' * 79)

        cursor.close()

    
    if choice == 4: # Dodaj kwote do skarbonki
        
        #db = sqlite3.connect("simple.db")
        #cursor = db.cursor()
        nazwa = input("Wpisz nazwę: ")
        ilość = int(input("Podaj kwote: "))
        id_invest = int(input("Podaj numer ID Skarbonki: "))

        #Zrobić transakcje
        cursor = db.cursor()
        cursor.execute(''' INSERT INTO fundusze
                            (NAZWA, KWOTA, invest_ID) 
                            VALUES (?, ?, ?);''', (nazwa, ilość, id_invest))
        cursor.execute(''' SELECT KWOTA FROM inwestycje WHERE ID = (?)  ''', str(id_invest))
        aktualnaKwota = cursor.fetchall()[0][0]
        
        cursor.execute('''UPDATE inwestycje SET KWOTA = (?) where inwestycje.ID=(?)''', (int(aktualnaKwota)+ilość, id_invest))
        #Zakończenie transakcji
        
        #commitMe()
        db.commit()
        print("Dane dodano poprwanie")
        db.close()
        

    if choice == 5: # Usuń Skarbonkę

         
        #db = sqlite3.connect("simple.db")
        #cursor = db.cursor()
        id = input("Wpisz ID Skarbonki: ")
        

        
        #cursor = db.cursor()
        cursor.execute(''' DELETE FROM
                                inwestycje 
                            WHERE
                                ID=(?);''',(id))
        
        db.commit()
        print("Dane dodano poprwanie")
        db.close()

    if choice == 6:
        zonda()

    if choice == 0: # Zamknij program 
           break

'''

UPDATE people
SET personal_expense = (
      SELECT SUM(amount)
      FROM expenses
      WHERE expenses.type = 'personal'
        AND expenses.name = people.name ),

    business_expense = (
      SELECT SUM(amount)
      FROM expenses
      WHERE expenses.type = 'business'
        AND expenses.name = people.name )

'''


# cursor.execute('''  UPDATE inwestycje
#                            SET kwota = (?)
#                           WHERE nazwa = (?); ''', (ilość, nazwa))



