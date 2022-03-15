import sqlite3
def insertMultipleData(Datalist):
    con = sqlite3.connect('student_db')

    cursor = con.cursor()

    insert_query = ''' INSERT INTO stud_marks VALUES(?,?,?)'''
    cursor.executemany(insert_query,Datalist)

    con.commit()
    print('Total records inserted:',cursor.rowcount)

    con.commit()
    con.close()

Datalist = [(4,'rajesh',89),(5,'anny',68),(7, 'shiv',87),(8,'tapan',85)]
insertMultipleData(Datalist)