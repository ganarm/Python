'''
import os
print("The Extension of ganesh.txt File is : ",os.path.splitext("ganesh.txt")[1])


def func1(name,age):
    print("Hello",name,"you are",age," year's old.")
func1("Ganesh",age=24)

def func2(*arg):
    sum=0
    for i in arg:
        sum=sum+i
    print(sum)

func2(1,2,5,2,2,55,2,2,2,7,8,8,5,5)

def countVowels(str1):
    count=0
    l=['A','E','I','O','U','a','e','i','o','u']
    print("Vowles are:",end=" ")
    for i in str1:
        if i in l:
            print(i,end=" ")
            count+=1
    print("\nTotal Count of Vowels:",count)
countVowels("Geeks for Geeks")

def printData(**d):
    for k,v in d.items():
        print(k," => ",v)
data1={'1':'Ganesh Mali','2':'Mitali Mahajan','3':'Komal Shinde'}
printData(**data1)

str1="Ganesh Mali from FY MSc(CS)"
print(str1[::-1])

a=str(input("Enter String : "))
print(a[::2])


 Write a Python function to get a string from a given string where all occurrences of 
its first char have been changed to ‘@', except the first char itself
'''
def func1(str1):
    a=str1[0]
    ns=""
    for i in str1:
        if i == a:
            ns=ns+'@'
        else:
            ns=ns+i
    ns[0]=a
    print(ns)
func1("Ganesh Mali Ganesh Ganesh GG")