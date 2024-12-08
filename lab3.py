'''
a=10
def func():
    global a
    a=1
    print(a)
func()
print(a)

def isPerfect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
        print(n,"is Perfect Number.")
    else:
        print(n,"is Not Perfect Number.")
isPerfect(6)

def chnage1(s):
    l=[]
    temp=''
    for i in s:
        if i not in l:
            temp=temp+'@'
            l.append(i)
        else:
            temp=temp+i
    print(s)
    print(temp)
chnage1("abcabcabc")

print(round(10.2554,2))


l=[1,2,2,323,3,2,2,5,5,2]
def square(a):
    return a*a
map1=map(square,l)
print(list(map1))


l=[1,-2,-2,-323,3,2,2,5,5,2]
f1=filter(lambda a:a<0,l)
print(list(f1))

from mod1 import *
print(sum(1,2))


import mod1
print(mod1.sum(1,2))

import mod1 as a
print(a.sum(3,4))



l=[4,5,52,2,414,11,44125,545,45,74,4]

w=map(lambda x:x+1,l)
print(list(w))


str1=input("Enter String : ")
print(str1[::-1])

for i in range(len(str1)-1,-1,-1):
    print(str1[i],end="")


#1

import area as a
r=int(input("Enter Radius : "))
print("Area of Circle (Radius ",r,") : ",a.areaOfC(r))


#2

from datetime import *
print(datetime.now())


#3
func1=lambda str1:str1[0].lower()=="a"
print(func1("Ajinkya"))


#4
import mod1 as a
print(a.fact(4))


#5
l=[1.22,1.35,45.99,74.36]
s1=[]
for i in l:
    s1.append(round(i))
print(s1)

l=[1.22,1.35,45.99,74.36]
print(list(map(round,l)))

#6
def abc(a):
    return round(a,1)
l=[1.22,1.35,45.99,74.36]
print(list(map(abc,l)))

#7

l1=[1,21,25,5,5,2]
l2=[5,52,22,5,5,4]
print(list(map(lambda a,b:a+b,l1,l2)))



def chnage1(s):
    l=[]
    temp=''
    for i in s:
        if i not in l:
            temp=temp+'@'
            l.append(i)
        else:
            temp=temp+i
    print(s)
    print(temp)
chnage1("abcabcabc")

'''
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[]
for i in range(0,len(l1),2):
    print(i)
    l2.append(l1[i])
        