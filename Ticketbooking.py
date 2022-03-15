class Ticketbooking:
    def bookicket(self):

    def removeticket(self):

    def choosemovie(self):
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