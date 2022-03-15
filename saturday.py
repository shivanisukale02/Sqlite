
import sqlite3

con = sqlite3.connect('customer_db')

cursor = con.cursor()

sqlite_query = ''' CREATE TABLE customer_details(id INTEGER PRIMARY KEY,name TEXT NOT NULL, city TEXT NOT NULL ,ticket INTEGER NOT NULL)'''

cursor.execute(sqlite_query)

print("Table is created successfully")

sqlite_insert_query = ''' INSERT INTO customer_details VALUES(1,'Shivani','Mahad',2) '''

cursor.execute(sqlite_insert_query)

print("customer record is inserted")
con.commit()
con.close()

import sqlite3
def insertData(name,id,city,ticket):
    con = sqlite3.connect('customer_db')

    cursor = con.cursor()

    insert_query = ''' INSERT INTO customer_details VALUES(?,?,?,?)'''
    cursor.execute(insert_query,(id,name,city,ticket))

    con.commit()

    con.close()
insertData(2,'tapan','chalisgaon',5)
insertData(3,'deepa','pune',3)

import sqlite3

con = sqlite3.connect('customer_db')

cursor = con.cursor()

sqlite_select_query = ''' SELECT * FROM customer_details'''

cursor.execute(sqlite_select_query)

records = cursor.fetchall()

print(records)
for row in records:
    print('id:',row[0])
    print('name:', row[1])
    print('city: ',row[2])
    print('tickets',row[3])

print(records.count(row))
con.close()
