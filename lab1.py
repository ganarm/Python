#Q1
'''
a=eval(input("Enter any data : "))
print("You Entered : ",a,"\n Data Type : ",type(a))
'''
#Q2
'''
name=str(input("Enter Your Name : "))
age=int(input("Enter Your Age : "))
print ("Hello, ",name,"You are ",age,"years old.")
'''
#Q3
'''
while(1):
    a=eval(input("Enter a : "))
    b=eval(input("Enter b : "))
    op=str(input("Enter operator : "))
    if (op=='+'):
        print(a," + ",b," : ",a+b)
    elif (op=='-'):
        print(a," - ",b," : ",a-b)
    elif (op=='*'):
        print(a," * ",b," : ",a*b)
    elif (op=='/'):
        print(a," / ",b," : ",a/b)
    elif (op=='//'):
        print(a," % ",b," : ",a%b)
    elif (op=='**'):
        print(a," ** ",b," : ",a**b)
    elif (op=='//'):
        print(a," // ",b," : ",a//b)
    else:
        print("Plz Enter Valid operatot")
    yes=eval(input("You want to Perform another operation (0:No / 1:Yes) : "))
    if(yes==0):
        break
'''
#Q4 Area and Perimeter of Rectangle
'''
width=eval(input("Enter Width of Rectangle : "))
length=eval(input("Enter length of Rectangle : "))
print("Area of Rectangle : ",length*width)
print("Perimeter of Rectangle : ",2*(length+width))
'''
#Q5 Even or Odd
'''
a=int(input("Enter No : "))
if a%2==0:
    print(a," is Even Number.")
else:
    print(a," id Odd Number.")
'''
#Q6
'''
p=eval(input("Enter Principle Amount : "))
r=eval(input("Enter Rate of Interest per Year: "))
t=eval(input("Enter Time Period in year : "))
print("Simple Interest : ",(p*r*t)/100)
'''
#Q7
'''
a=int(input("Enter 1st Number : "))
b=int(input("Enter 2nd Number : "))
c=int(input("Enter 3rd Number : "))
print("Average : ",(a+b+c)/3)
'''
#8
'''
ttype=str(input("Enter Temperature type you enter Fahrenheit(F) or Celcius (C): "))
a=int(input("Enter Temperature : "))
if (ttype=="F"):
    print("Temperature in Celcius : ",5/9*(a-32))
else:
    print("Temperature in Fahrenheit : ",(a*9/5)+32)
'''
#9
'''
h=eval(input("Enter Height : "))
w=eval(input("Enter Weight : "))
bmi=w/(h**2)
print("BMI : ",bmi)
if(bmi >= 18.5 and bmi <=25):
    print("Normal")
elif(bmi > 25):
    print("Over Weight")
elif(bmi>17 and bmi<18.5):
    print("Thiness")
else:
    print("plz give correct input")
'''
#10

a=eval(input("Enter a : "))
b=eval(input("Enter b : "))

if a==b:
    print(a,"is Equal to",b)
if a!=b:
    print(a,"not equal to",b)
if a>b:
    print(a,"is greater than ",b)
else:
    print(b,"is greater than ",a)

