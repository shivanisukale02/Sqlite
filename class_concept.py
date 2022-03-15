class student:
    '''This is student class
    we are learning class concepts'''
    def __init__(self,name,dept):
        self.name = name
        self.dept = dept
    def printName(self):
        print('name of student is' ,self.name)

stud1 = student('Reject','CSE')
stud2 = student('vignesh','IT')

stud1.printName()
stud2.printName()

print('-'*50)

stud2.name = 'vicky'
stud2.printName()