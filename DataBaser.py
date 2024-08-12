DataBaser.py
import Sqlite3
Conn = sqlite3.connect("UserData.db")

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS Users (
               1d INTERGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Name TEXT NOT NULL,
               Email TEXT NOT NULL,
               User TEXT NOT NULL,
               Password TEXT NOT NULL
               );
               """)

print ("Conectado ao Banco de Dados")