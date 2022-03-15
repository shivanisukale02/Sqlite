
import sqlite3
def insertData(name,id,city,ticket):
    con = sqlite3.connect('customer_db')

    cursor = con.cursor()

    insert_query = ''' INSERT INTO customer_details VALUES(?,?,?,?)'''
    cursor.execute(insert_query,(name,id,city,ticket))

    con.commit()

    con.close()
insertData('tapan',2,'chalisgaon',5)
insertData('deepa',3,'pune',3)
