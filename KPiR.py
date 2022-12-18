import sqlite3
from menu import menu, menu_sprzedaz, menu_koszt, menu_daniny, menu_inwestycje, menu_inwestycje_skarbonki
from db import db_create_kpir, db_create_kalendarz, db_create_fundusze, db_create_inwestycje

db_create_kpir()
db_create_kalendarz()
db_create_fundusze()
db_create_inwestycje()

db = sqlite3.connect("simple.db")
cursor = db.cursor()

while True: #Główne Menu

    menu()
    choice_menu = (input("Wybierz opcje: "))
#==================================================================================================
#==================================================================================================
# Potrzebna jest funkcja. Jeżeli wpisana data, od 2022-12-01 do 2022-12-31 dodaj dateID 12/22

    if choice_menu == '1':  # SPRZEDAŻ
        

        while True:
            menu_sprzedaz()
            choice_sprzedaz = input("Wybierz opcję: ")
#-----------------------------------------------------------------------------------------------------------
            if choice_sprzedaz == "1": # Pokaż sprzedaż
                print("### POKAŻ SPRZEDAŻ ####")
                dt = input("Podaj data_id: ")

                cursor.execute(f'''
                    SELECT 
                        SUM(Wartość)
                    FROM 
                        kalendarz
                    WHERE
                        Data_id = '{dt}'
                ''')
                
                
                rows = cursor.fetchall()

                for x in rows:
                    print("Suma :", x[0])

                
#-----------------------------------------------------------------------------------------------------------
            if choice_sprzedaz == "2": # Dodaj godziny
                print("### DODAJ GODZINY ###")
                dt = input(" Podaj datę: ")
                dt_id = input("Podaj data_id: ")
                rg = int(input('Podaj ilość godzin: '))
                st = int(input("Podaj stawkę: "))
                wr = rg * st
                vat = 1.23
                brt = wr * vat
                w_vat = brt - wr

                db.execute('INSERT INTO kalendarz (Data, Data_ID, Godziny, Stawka, Wartość, S_VAT, W_VAT, W_Brutto) VALUES (?, ?, ?, ?, ?, ?, ?, ?);',(dt, dt_id, rg, st, wr, vat, w_vat, brt))   
                db.commit()
                
                
#-----------------------------------------------------------------------------------------------------------
            if choice_sprzedaz == "3": # Pokaż godziny
                print("### POKAŻ GODZINY ###")

                cursor.execute('SELECT * FROM kalendarz GROUP BY Data')
                
                rows = cursor.fetchall()
                
                for x in rows:
                    print("+" +'-' * 17 + "+")
                    print( "|Data: ",    x[1])
                    print( "|Data_ID: ", x[2])
                    print( "|Godziny: ", x[3])
                    print( "|Stawka: ",  x[4])
                    print( "|Netto: ", x[5])
                    print( "|VAT%: ", x[6])
                    print( "|VAT: ", x[7])
                    print( "|Brutto: ", x[8])
                    print("+" +'-' * 17 + "+")

                

                
#-----------------------------------------------------------------------------------------------------------
            if choice_sprzedaz == "0": # Wróć do menu
                print("### WRÓĆ ###")
                break
#==================================================================================================
#==================================================================================================      
    if choice_menu == '2': # ZAKUPY
         

        while True:
            menu_koszt()
#-----------------------------------------------------------------------------------------------------------            
            choice_zakup = int(input("Wybierz opcje: "))
            if choice_zakup == 1: # Pokaż zakupy
                print("### POKAŻ ZAKUPY ###")
                cursor.execute('''
                SELECT 
                    ID,
                    Data,
                    Data_ID,
                    Ilość,
                    Netto,
                    P_VAT,
                    W_VAT,
                    Brutto
                FROM
                    koszty
                GROUP BY Data        
                ''')
                rows_2 = cursor.fetchall()

                for x in rows_2:
                    print("----------------")
                    print("ID :", x[0])
                    print("Data :", x[1])
                    print("Data_ID :", x[2])
                    print("Ilość :", x[3])
                    print("Netto :", x[4])
                    print("VAT% :", x[5])
                    print("VAT :", x[6])
                    print("Brutto :", x[7])
                    print("-----------------")
                    
                
#-----------------------------------------------------------------------------------------------------------
            if choice_zakup == 2:  # Dodaj zakupy
                print("### DODAJ ZAKUP ###")

                    

                dt_k  = input("Podaj datę: ")
                dt_id = input("Podaj data_id: ")
                il = input("Podaj ilość: ")
                net = float(input("Podaj wartość netto: "))
                vat = 1.23
                bru = net * vat
                w_vat = bru - net
                cursor.execute('''
                    INSERT INTO koszty
                        (Data, 
                        Data_ID,
                        Ilość,
                        Netto,
                        P_VAT,
                        W_VAT,
                        Brutto)
                    VALUES
                        (?, ?, ?, ?, ?, ?, ?);''', (dt_k, dt_id, il, net, vat, w_vat, bru))
                db.commit()
                    
            if choice_zakup == 0:  # Wróc do menu
                print("### WRÓĆ ###")
                break    
#==================================================================================================
#=======================================================================================================
    if choice_menu == '3':  # DANINY        
        while True:
            menu_daniny()
            choice_daniny = input("Wybierz opcję: ")
            
            if choice_daniny == "1":
                print("### PODATEK DOCHODOWY ###")
                cursor.execute('''               
                
                SELECT kalendarz.Data_ID, (kalendarz.Wartość)-(sum(koszty.Netto))  
                FROM kalendarz
                INNER JOIN koszty
                WHERE kalendarz.Data_ID = koszty.Data_ID''')
                # Dochód = przychód - koszty
                # Podatek = dochód * 12% - 300
            if choice_daniny == "2":
                print("### VAT ###")
            if choice_daniny == "3":
                print("### ZUS ###")
            if choice_daniny == "0":
                print("### WRÓĆ ###")


        
     

        
#==================================================================================================
#=======================================================================================================
    if choice_menu == '4': # INWESTYCJE
       # menu_inwestycje()

        
#---------------------------------------------------------------------------------
        while True:
            menu_inwestycje()
            choice_invest = input("wybierz opcje: ")            
            if choice_invest == "1": # Skarbonka
               
                while True:
                    menu_inwestycje_skarbonki()
                    choice_invest_skarb = input("Wybierz opcje: ")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    if choice_invest_skarb == "1": # POKAŻ SKARBONKI
                        print("### POKAŻ SKARBONKI ###")
                        cursor.execute(''' SELECT 
                                inwestycje.ID,
                                inwestycje.NAZWA,
                                inwestycje.WARTOŚĆ,
                                inwestycje.KWOTA
                            FROM 
                                inwestycje ''')

                    rows = cursor.fetchall()
                    
                    for x in rows:
                        print("-" * 79)
                        print( "ID: ", x[0])
                        print( "Nazwa: ", x[1])
                        print( "WARTOŚĆ: ", x[2])
                        print( "Kwota: ", x[3])
                        print('-' * 79)

                    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    if choice_invest_skarb == "2": # DODAJ SKARBONKĘ
                        print("### DODAJ SKARBONKI ###")
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
                                                                                            
                            db.commit()

                        except sqlite3.Error as e:
                            print("Error -> Coś poszło nie tak", e)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    if choice_invest_skarb == "3": # POKAŻ WPŁATY
                        print("### POKAŻ WPŁATY ###")
                        cursor.execute(''' SELECT 
                                        invest_ID,
                                        NAZWA, 
                                        KWOTA
                                    FROM 
                                        fundusze
                                    GROUP BY ID ''')

                    rows = cursor.fetchall()
                    for x in rows:
                        print("-" * 79)
                        print( "ID: ", x[0])
                        print( "Nazwa: ", x[1])
                        print( "Kwota: ", x[2])
                        print('-' * 79)

                    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                    if choice_invest_skarb == "4": # DODAJ WPŁATE
                        print("### DODAJ WPŁATE ###")
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
                        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                
                    if choice_invest_skarb == "5":
                        print("### USUŃ SKARBONKE ###")
                                
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

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                
                    if choice_invest_skarb == "0":
                        print("### WRÓC ###")
                        break
    #---------------------------------------------------------------------------------
            if choice_invest == '2': # KRYPTOWALUTY
                break
    #---------------------------------------------------------------------------------
            if choice_invest == '3': # GIEŁDA
                break
    #---------------------------------------------------------------------------------
            if choice_invest == '0': # WRÓĆ
                print("### WRÓĆ ###")
                break
#---------------------------------------------------------------------------------
        
#==================================================================================================        
#=======================================================================================================
        
    if choice_menu == '0': # ZAMKNIJ PROGRAM
        db.close()
        break

