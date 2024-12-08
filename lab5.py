
'''
file=open('tmpfile.txt','a')
# print(file)
if(file.write("Hii...Ganesh Mali ")):
    print("Data Inserted Successfully....!!")
'''
# List Compression
# l1=[1,2,22,22,22,5,5,522,2,5,5,2,2,2,2,2,2,22,2,2,22,26]
'''
l1=[i**2 for i in range(1,21)]
print("Sqaure of Numbers from 1 to 20 : ",l1)
print("\n")
l1=[i**2 for i in range(1,21) if (i%2==0)]
print("Sqaure of Even Numbers between 1 to 20 : ",l1)
'''
'''
file=open('tmpfile.txt',"r")
data=eval(input("Enter Number : "))
data=file.readline(data)
print(data)
'''
'''
l1=[(1,"Ganesh"),(2,"Ajinkya"),(3,"Sunil"),(4,"Prathmesh")]

l2=sorted(l1,key=lambda x:x[1])
print(l2)
'''
'''
while(1):
    print("** Opeartions on File **")
    print("1. Open File")
    print("2. Read from a File")
    print("3. Write in a File")
    print("4. Append in a File")
    print("5. Readline in a File")
    print("6. Writeline in a File")
    print("7. Close a File")
    print("8. Rename a File")
    print("9. Exit")
    c=int(input("Enter Your Choice : "))
    if (c==9):
        break
    elif (c==1):
        file=open('tmpfile.txt')
        if(file):
            print("File Open Successfully")
    
    elif(c==2):
        data=''
        file=open('tmpfile.txt',"r")
        data=file.read()
        print(data)

    elif(c==3):
        file=open('tmpfile.txt',"w")
        data=input("Enter Data Want to Insert : ")
        if(file.write(data)):
            print("Data Inserted Successfully....!!")
    elif(c==4):
        file=open('tmpfile.txt',"a")
        data=input("Enter Data Want to Insert : ")
        if(file.write(data)):
            print("Data Inserted Successfully....!!")
    elif(c==5):
        file=open('tmpfile.txt',"r")
        while True:
            line = file.readline()
            if not line:  # If line is empty, end of file is reached
                break
            print("Lines :", line)
    elif(c==6):
        data = input("Enter Data to Write : ")
        file = open('tmpfile.txt', "w")
        file.writelines([data + '\n'])  # Write the data as a new line
        print("Data Written Successfully!")
    elif(c==7):
            file.close()
            print("File Closed Successfully!")
    elif(c==8):
        new_name = input("Enter New File Name : ")
        import os
        os.rename('tmpfile.txt', new_name)
        print("File Renamed Successfully!")
    else:
        print("Invalid choice. Please try again.")

'''
'''
people={
    'Ganesh':{'age':22,'city':'Nashik'},
    'Ajinkya':{'age':23,'city':'Pune'},
    'Prethmesh':{'age':21,'city':'Nashik'}
}

for i,j in people.items():
    if (j['age']>20 and j['city']=='Nashik'):
        print(i)
'''
'''
file=open("input.txt","r")
data=file.read()
print(data)
data1=data[::-1]
file=open('output.txt',"w")
if(file.write(data1)):
    print("Data Inserted Successfully....!!")
'''
'''
src=input("Enter Source File Name : ")
dest=input("Enter Destination File Name : ")
file=open(src,"r")
data=file.read()
print("Data in File : ",data)
file=open(dest,"w")
if(file.write(data)):
    print("Data Inserted Successfully....!!")
'''
'''
file=open("input.txt","r")
data=file.read()
print("Data in File : ",data)
l1=data.split()
dict1={}
for i in l1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i]=dict1[i]+1
print(dict1)
'''
file=open('tmpfile.txt',"r")
line = file.readlines(2)
print(line)
'''
while True:
    line = file.readlines(2)
    if not line:  
        break
    print("Lines :", line)

'''
'''
data=["ganaesh\n","ajinkya\n","Prathmesh"]
file.writelines(data)
'''
