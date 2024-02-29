import csv
import mysql.connector

def citeste_csv_si_insereaza(worldcities, orase):  
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="199601wasD",
            database="orase"
        )
        cursor = mydb.cursor()

        with open('F:\Probleme Python\worldcities\worldcities.csv ' , 'r') as csvfile:
            cititor_csv = csv.reader(csvfile)
            for row in cititor_csv:
                col1, col2, col3 , col4 , col5 , col6 = row 

                cursor.execute("INSERT INTO nume_tabel (col1, col2, col3) VALUES (%s, %s,%s,%s,%s,%s)",
                               (col1, col2, col3, col4 , col5 , col6))
                mydb.commit()

        print("Datele au fost inserate cu succes în baza de date.")
    except Exception as e:
        print(f"Eroare: {str(e)}")
    finally:
        mydb.close()

nume_fisier_csv = 'F:\Probleme Python\worldcities\worldcities.csv'
nume_baza_de_date = 'orase'
citeste_csv_si_insereaza('F:\Probleme Python\worldcities\worldcities.csv', 'orase')
