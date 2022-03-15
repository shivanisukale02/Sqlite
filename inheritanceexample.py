'''
#parent class
class Animal:
    def speak(self):
        print("Animal is speaking")

#child class
class lion(Animal):
    def roar(self):
        print("lion is roaring")
simba= lion()
simba.roar()


#multiple inheritance
class Calc1:
    def addition(self,a,b):
        return a+b
'''
'''
class Calc2:
    def multiplication(self,a,b):
        return a*b

class Calc3(Calc1,Calc2):
    def substraction(self,a,b):
        return a-b

a=Calc3()
print(a.substraction(5,4))
print(a.multiplication(5,4))
print(a.addition(5,4))

print(issubclass(Calc3,Calc1))
'''
'''
class A:
    def mk(self):
        print("i am from class A")

class B:
    def mk(self):
        print("i am from calss B")

class C(A,B):
    def __init__(self):
        print("class c is getting constructed")

f=C()
f.mk()

#method overriding
class D():
    def  mk(self):
        print("i am in class D")

v=D()
v.mk()
'''
'''
#abstraction

class Student:
    count=0
    def __init__(self):
        Student.count +=1
    def printCount(self):
        print("count is:",Student.count)

stud1 = Student()
print(stud1.count)
stud1.printCount()
'''
class Student:
    __count=0
    def __init__(self):
        Student.__count +=1
    def printCount(self):
        print("count is:",Student.__count)

stud1 = Student()
print(stud1.count)
stud1.printCount()