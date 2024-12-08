'''
import datetime
print(datetime.datetime.now())

t1=(1,2,4,5,6,6,3,3)
e1,e2,*e3=t1
print(e1)
print(e2)
print(e3)

l1=[1,2,3,4,5,6]
l1.append(7)
print(l1)
l1.extend([9,7,5,6])
print(l1)
l1.insert(1,10)
print(l1)
l2=sorted(l1)
print(l2)
l1.sort()
print(l1)

from math_operations.basic_operations import *
print("Sum : ",sum(1,2))
print("Diff : ",diff(1,2))
print("Mul : ",mul(1,2))
print("Div : ",div(1,2))
from math_operations.advanced_operations import *
print("Power : ",pow(1,2))
print("Square Root : ",sqr(2))

dict1={'Ram':85,'Sham':92,'Ojas':88,'Anay':79}
print("Original Dictionary : ",dict1)

a1=filter(max,dict1.values())
print(type(a1))

print("Values : ",dict1.values())
print("")


dict1={'Ram':85,'Sham':92,'Ojas':88,'Anay':79}
print("Original Dictionary : ",dict1)

max1=0
name=''
for i,j in dict1.items():
    if (max1<j):
        name=i
        max1=j
print("Name : ",name," Marks : ",max1)

dict1['abc']=12


employee_data=("John","Doe",34,"Developer","New York")
(fname,lname,age,des,c)=employee_data
print("first name : ",fname," last name : ",lname,"age : ",age,"des : ",des,"City :",c)
 
l2=list(employee_data)
l2.append("Full Time")
print(l2)

skills_A={'Python','Java','SQL'}
skills_B={'Python','HTML','CSS'}
print("Skills in both : ",skills_A&skills_B)
print("Skills Unique to A : ",skills_A-skills_B)
print("The Union : ",skills_A|skills_B)


p=lambda a,b:a**b
print(p(2,3))

l1=[1,21,25,5,5,2]
l2=[5,52,22,5,5,4]
print(list(map(lambda a,b:a+b,l1,l2)))

l=[4,3,2,2,5,5,2]
f1=filter(lambda a:a%2==0,l)
print(list(f1))

l1=[1,21,25,5,5,2,2,5,6,3,9]
s1=set(l1)
print(l1,"\n",s1)
l2=list(s1)
print(l2)

