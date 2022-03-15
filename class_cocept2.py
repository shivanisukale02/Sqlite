class student:
    '''This is student class
    we are learning class concepts'''
    studentcount = 0
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept
        student.studentcount += 1

    def printName(self):
        print('name of student is' ,self.name)

    def printCount(self):
        print('no of student:' ,student.studentcount)


stud1 = student('Reject','CSE')
stud2 = student('vignesh','IT')

#stud1.printName()
#stud2.printName()

#print('-'*50)

#stud2.name = 'vicky'
#stud2.printName()

stud1.printCount()