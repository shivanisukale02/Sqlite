import sqlite3

con = sqlite3.connect('student_db')

cursor = con.cursor()

sqlite_query = ''' CREATE TABLE stud_marks(id INTEGER PRIMARY KEY, name TEXT NOT NULL, marks INTEGER NOT NULL)'''

cursor.execute(sqlite_query)

print("Table is created successfully")

sqlite_insert_query = ''' INSERT INTO stud_marks VALUES(1000,'TOM',95) '''

cursor.execute(sqlite_insert_query)

print("student record is inserted")

con.commit()

con.close()