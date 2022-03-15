import sqlite3
def insertData(id,name,marks):
    con = sqlite3.connect('student_db')

    cursor = con.cursor()

    insert_query = ''' INSERT INTO stud_marks VALUES(?,?,?)'''
    cursor.execute(insert_query,(id,name,marks))

    con.commit()

    con.close()
insertData(2,'sam',85)
insertData(3,'ram',75)
