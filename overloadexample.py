'''
class A:
    def myCalculate(self, x=None ,y= None):
        if x!=None and y!= None:
            return x + y
        elif x!= None:
            return x**2
        else:
            return 0

res = A()
print("zero argument",res.myCalculate())
print("one argument",res.myCalculate(5))
print("two argument",res.myCalculate(5,2))
'''
class A:
    def __init__(self,num):
        self.num = num

    def __add__(self, other):
        self.num + other.num

    def __eq__(self, other):
        if self.num == other.num:
            return" self and other are equal"
        else:
            return " self and other are equal"

obj1 =A(2)
obj2 = A(3)

print(obj1.num)
print(obj2.num)
print(obj1 + obj2)
print(obj1 ==obj2)