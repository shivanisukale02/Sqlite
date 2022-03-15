import sqlite3

con = sqlite3.connect('customer_db')

cursor = con.cursor()

sqlite_select_query = ''' SELECT * FROM customer_details'''

cursor.execute(sqlite_select_query)

records = cursor.fetchall()

print(records)
for row in records:
    print('name:',row[0])
    print('id:', row[1])
    print('city: ',row[2])
    print('tickets',row[3])



con.close()
