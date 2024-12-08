'''
class Sample():
    a,b=0,0
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(a+b)
s1=Sample(1,2)
s1.add()
'''

'''
class Car():
    def __init__(self,brand,year,color):
        self.brand=brand
        self.year=year
        self.color=color
    def display_info(self):
        print(" Brand : ",self.brand,"\n Year : ",self.year,"\n Color : ",self.color)
c1=Car("A Brand",2001,"Black")
c1.display_info()
'''

'''
class Employee():
    def __init__(self,a,b,c):
        self.name=a
        self.pos=b
        self.sal=c
    def display(self):
        print(" Name : ",self.name,"\n Position : ",self.pos,"\n Salary : ",self.sal)
e1=Employee("Harish","Team Manager",45000)
e1.display()
'''
'''
import time
class Animal():
    def speak(self):
        print("Animation Sound")

class Dog(Animal):
    def speak(self):
        print("Bho Bho")

class Cat(Animal):
    def speak(self):
        print("Myaav Myaav")
d=Dog()
c=Cat()
while(1):
    d.speak()
    time.sleep(1)
    c.speak()
    time.sleep(1)
'''
'''
class Vehicle():
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
    def display_info(self):
        print(" Brand : ",self.brand,"\n Speed : ",self.speed)
class Car(Vehicle):
    def __init__(self,brand,speed,milege):
        super().__init__(brand,speed)
        self.milege=milege
    def display_info(self):
        super().display_info()
        print("Milege : ",self.milege)
c1=Car("abc",120,50)
c1.display_info()
'''
'''
class Engine():
    def __init__(self,h):
        self.horsepower=h   
    def display_info(self):
        print(" HP : ",self.horsepower)
class Body():
    def __init__(self,m):
        self.material=m 
    def display_info(self):
        print(" Body : ",self.material)

class Car(Engine,Body):
    def __init__(self,h,m):
        super().__init__(h)
        Body.__init__(self,m)
    def display_info(self):
        super().display_info()
        Body.display_info(self)
c=Car(1200,"Steel")
c.display_info()
'''
'''
# Single Level 
class A():
    def __init__(self):
        print("This is class : A")

class B(A):
    def __init__(self):
        super().__init__()
        print("This is class : B")

b=B()

# Multi Level 

class A():
    def __init__(self):
        print("This is class : A")

class B(A):
    def __init__(self):
        super().__init__()
        print("This is class : B")
class C(B):
    def __init__(self):
        super().__init__()
        print("This is class : C")
c=C()

# Mutiple 

class A():
    def __init__(self):
        print("This is class : A")

class B():
    def __init__(self):
        print("This is class : B")

class C(A,B):
    def __init__(self):
        super().__init__()
        B.__init__(self)
        print("This is class : C")
c=C()

# Hiearachical 
class A():
    def __init__(self):
        print("This is class : A")

class B(A):
    def __init__(self):
        super().__init__()
        print("This is class : B")
class C(A):
    def __init__(self):
        super().__init__()
        print("This is class : C")
c=C()
b=B()
'''