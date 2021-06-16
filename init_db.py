import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE trainingData (uid TEXT , sentence TEXT, intent TEXT)')
print("Table created successfully");
conn.close()
