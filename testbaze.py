import sqlite3

conn = sqlite3.connect('site.db')

c = conn.cursor()

c.execute('SELECT * FROM User;')