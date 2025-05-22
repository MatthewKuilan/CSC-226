import sqlite3

# connection object
conn = sqlite3.connect("C:\\Users\\Matthew\\Desktop\\fourthdb.db")

cursor = conn.cursor()

cursor.execute(" insert into Students(Name, Age) values ('Mark', 3000) ")
name = cursor.execute(" select Name from students where Name = 'Matthew' ")
conn.commit()
conn.close()
