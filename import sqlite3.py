import sqlite3
banco = sqlite3.connect('banco1.db')

cursor = banco.cursor()
cursor.execute("CREATE TABLE pessoas (nome text,idade integer, email text)")