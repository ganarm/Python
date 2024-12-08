'''
def area_of_rectangle(l,w):
    print("Area of Rectangle : ",end=" ")
    print(l*w)
l=float(input("Enter Length : "))
w=float(input("Enter Width : "))
area_of_rectangle(l,w)

vowels=['a','e','i','o','u','A','E','I','O','U']
c=0
s=input("Enter String : ")
for i in vowels:
    if (i in s):
        c=c+1
print("Total Vowels : ",c)


def sum_i(*args):
    s=0
    for i in args:
        s=s+i
    print("Sum : ",s)
a=[]
b=eval(input("Enter n : "))
for i in range(0,b):
    t=eval((input("Enter no. : ")))
    a.append(t)
sum_i(*a)


def print_details(**args):
    uk=eval(input("Enter Key : "))
    for k,v in args.items():
        if uk==k:
            print(k," => ",v)
d={'1':'ganesh','2':"arin",'3':"ajinkya"}
print_details(**d)



def greet(name,msg="Hello"):
    print(msg+" "+name)

greet('Ganesh')
greet('Arin','Bye')



s=str(input("Enter String : "))
print("Reverse String : ",s[::-1])

a=eval(input("Enter List : "))
print("Sub List : ",a[1:len(a):2])



d={1:'ganesh',2:'arin',3:'ajinkya'}
print("Original : ",d)
d[4]="prathmesh"
print("Add New : ",d)
d[1]="sanat"
print("Update : ",d)
d.pop(1)
print("Delete : ",d)


def multiply(a,*args):
    for i in args:
        print(a*i)
l=[1,2,3,3]
multiply(5,*l)
'''
a=2
while(a!=0):
    print(a)
    a=a-1
else:
    print("else")

for i in range(5):
    print(i)
else:
    print("else")