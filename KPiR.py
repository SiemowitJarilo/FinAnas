import sqlite3
from menu import kpir_menu_koszt, kpir_menu, kalendarz_menu
from db import db_create_kpir, db_create_kalendarz

db_create_kpir()
db_create_kalendarz()

db = sqlite3.connect("simple.db")
cursor = db.cursor()

while True:

    kpir_menu()
    choice = (input("Wybierz opcje: "))

#==================================================================================================
# Potrzebna jest funkcja. Jeżeli wpisana data, od 2022-12-01 do 2022-12-31 dodaj dateID 12/22

    if choice == '1': 
        kalendarz_menu()

        while True:
            choice3 = input("Wybierz opcję: ")

            if choice3 == "1":
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

                kalendarz_menu()

            if choice3 == "2":
                
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
                
                kalendarz_menu()

            if choice3 == "3":

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

                

                kalendarz_menu()

            if choice3 == "0":
                break
 #==================================================================================================      
    if choice == '2':
        kpir_menu_koszt()    

        while True:
            
            choice_2 = int(input("Wybierz opcje: "))
            if choice_2 == 1:
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
                

            if choice_2 == 2:    

                    

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
                    
            if choice_2 == 0:
                break    
#=======================================================================================================
    if choice == '3':          
        

        
     
        # VAT do zapłaty: 
        break

#=======================================================================================================

        
    if choice == '0':
        db.close()
        break

