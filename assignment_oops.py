'''
class Power:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(Power().pow(-5, 2))
'''
'''
class Solution(object):
   def myPow(self, x, n):
      power = abs(n)
      res = 1.0
      while power:
         if power & 1:
            res*=x
         x*=x
         power>>=1
      if n<0:
         return 1/res
      return res
ob1 = Solution()
print(ob1.myPow(45, 1))
print(ob1.myPow(21, 3))
'''

'''
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14


Circle2 = Circle(3)
print("area: ",Circle2 .area())
print("perimeter :", Circle2 .perimeter())
'''
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x=0, y=0):
        self.x += 1
        self.y += 1
        return self.x, self.y
x1 =Point(2,3)
print("show",x1.show())
print("moved",x1.move())

