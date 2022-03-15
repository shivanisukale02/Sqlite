#shivani sukale
import sqlite3
con = sqlite3.connect('employee_management.db')
cursor = con.cursor()
sqlite_query = '''CREATE TABLE Employee_detail(empCode INTEGER PRIMARY KEY, name TEXT NOT NULL,
phone TEXT NOT NULL, email TEXT NOT NULL, designation TEXT NOT NULL,
salary REAL NOT NULL, company_name TEXT NOT NULL);'''
cursor.execute(sqlite_query)
print('table is created successfully')
def Add_Employ_details(): #add employee details
     Emp_Code = input("Enter Employee Code : ")
     Name = input("Enter Employee Name : ")
     Phone_no = input("Enter Employee's phone no. : ")
     Email = input("Enter Employee's email : ")
     Designation = input("Enter Designation : ")
     Salary = input("Enter Employee Salary : ")
     Company = input("Enter Company Name : ")
     data = (Emp_Code, Name, Phone_no, Email, Designation, Salary, Company)
     insert_query = '''INSERT INTO Employee_detail VALUES (?,?,?,?,?,?,?)'''
     cursor.execute(insert_query, data)
     con.commit()
     print("Employee Added Successfully\n ")
     main()
def Display_Employees():  #display employee details
     sqlite_select_query = '''SELECT * FROM Employee_detail'''
     cursor.execute(sqlite_select_query)
     records = cursor.fetchall()
     print(records)
     for row in records:
         print('Emp_Code: ', row[0])
         print('Name: ', row[1])
         print('Phone_No.: ', row[2])
         print('Email: ', row[3])
         print('Designation: ', row[4])
         print('Salary: ', row[5])
         print('Company Name: ', row[6])
         print("------------")
         # con.close()
     main()

def Search(): #search emplyee by its name
     Name = input("enter Employee Name : ")
     sqlite_select_query = '''SELECT * FROM Employee_detail
     WHERE name = ?'''
     cursor.execute(sqlite_select_query, (Name,))
     records = cursor.fetchall()
     print(records)
     for row in records:
         print('Emp_Code: ', row[0])
         print('Name: ', row[1])
         print('Phone_No.: ', row[2])
         print('Email: ', row[3])
         print('Designation: ', row[4])
         print('Salary: ', row[5])
         print('Company Name: ', row[6])
     # con.close()
     main()

def Update(): #update detail by employees code
     Emp_Code = input("Enter Employee Code : ")
     Name = input("Enter Employee Name : ")
     Phone_no = input("Enter Employee'sphone no. : ")
     Email = input("Enter Employee's email : ")
     Designation = input("Enter Designation : ")
     Salary = input("Enter Employee Salary : ")
     Company = input("Enter Company Name : ")
     updt_query = '''UPDATE Employee_detail
     SET name = ?,phone = ?, email = ?,designation = ?,
     salary = ?, company_name = ?
     WHERE empCode = ?'''
     data = (Name, Phone_no, Email, Designation, Salary, Company, Emp_Code)
     cursor.execute(updt_query, data)
     con.commit()
     print("Total", cursor.rowcount, "Records updated successfully")
     con.commit()
     # con.close()
     main()

def Delete():  #Delete an employee using employee Code
     Emp_Code = input("Enter Employee Code : ")
     sqlite_delete_query = '''DELETE FROM Employee_detail
     WHERE empCode = ?'''
     cursor.execute(sqlite_delete_query, (Emp_Code,))
     con.commit()
     print("Employee Deleted")
     # con.close()
     main()

def Display_Employees_detail():  #Display all the details of employees whose salary is greater than 50000
     sqlite_select_query = '''SELECT * FROM Employee_detail
     WHERE salary > 50000'''
     cursor.execute(sqlite_select_query)
     records = cursor.fetchall()
     print(records)
     for row in records:
         print('Emp_Code: ', row[0])
         print('Name: ', row[1])
         print('Phone_No.: ', row[2])
         print('Email: ', row[3])
         print('Designation: ', row[4])
         print('Salary: ', row[5])
         print('Company Name: ', row[6])
     # con.close()
     main()

def Count_employees():  #Display the count of total number of employees in the company
     sqlite_count_query = '''SELECT COUNT(name) FROM Employee_detail'''
     cursor.execute(sqlite_count_query)
     count_employee = cursor.fetchone()
     print('total no of employees : ', count_employee[0])
     main()


def range():  # Display all the employee details, salary range
     min_salary = input('Enter min salary range: ')
     max_salary = input('Enter max salary range: ')
     sqlite_select_query = '''SELECT * FROM Employee_detail
     WHERE salary BETWEEN ? AND ?
    ORDER BY name ASC'''
     data = (min_salary, max_salary)
     cursor.execute(sqlite_select_query, data)
     records = cursor.fetchall()
     print(records)
     for row in records:
         print('Emp_Code: ', row[0])
         print('Name: ', row[1])
         print('Phone_No.: ', row[2])
         print('Email: ', row[3])
         print('Designation: ', row[4])
         print('Salary: ', row[5])
         print('Company Name: ', row[6])
     # con.close()
     main()

def Display_Avg(): #Display all the employees data, whose salary is less than the average salary of all the employees
     sqlite_select_query = '''SELECT * FROM Employee_detail
     WHERE salary < (SELECT avg(salary)FROM Employee_detail)'''
     cursor.execute(sqlite_select_query)
     records = cursor.fetchall()
     print(records)
     for row in records:
         print('Emp_Code: ', row[0])
         print('Name: ', row[1])
         print('Phone_No.: ', row[2])
         print('Email: ', row[3])
         print('Designation: ', row[4])
         print('Salary: ', row[5])
         print('Company Name: ', row[6])
     # con.close()
     main()
def main():
     print("\n\nEnter below no to perform following operations ")
     print("To Add Employee enter1 ")
     print("To View All employees enter2 ")
     print("To Search an employee using employee name enter3")
     print("To Update an employee details using employee Code ente4")
     print("To Delete an employee using employee Code enter5")
     print("To Display all the details of employees whose salary is greater than 50000 enter6")
     print("To Display the count of total number of employees in the company enter7")
     print("To Display all the employee details in alphabetical order,within the specific salary range enter8")
     print("To Display the employees data, whose salary is less than the average salary of all the employees enter9")
     print("To Exit enter10")
     ch = int(input("Enter your Choice "))
     if ch == 1:
        Add_Employ_details()
     elif ch == 2:
        Display_Employees()
     elif ch == 3:
        Search()
     elif ch == 4:
        Update()
     elif ch == 5:
        Delete()
     elif ch == 6:
        Display_Employees_detail()
     elif ch == 7:
        Count_employees()
     elif ch == 8:
        range()
     elif ch == 9:
        Display_Avg()
     elif ch == 10:
        exit(0)
     else:
        print("Invalid Choice")
        main()
main()
