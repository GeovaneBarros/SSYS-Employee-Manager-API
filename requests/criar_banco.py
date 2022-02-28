import sqlite3
con = sqlite3.connect('banco.db')

cur = con.cursor()

cur.execute('''CREATE TABLE controle (operacao text, sistema text)''')

cur.execute('''CREATE TABLE usuario
               (name text, email text, department text, salary real,birth_date text)''')

con.commit()

con.close()