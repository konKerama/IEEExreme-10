string=input()
a=string.split(" ",2)
n=int(a[0])
string1=(a[1])
symbols=[]
numbers=[]

for i in range(0,n):
    symbols.append(string1[i])
    numbers.append(i)
#symbols=a[1].split("",n)
#print(symbols)
firstAdd=input()
secondAdd=input()
addLine=input()
question=input()

frst=firstAdd.strip()

temp=secondAdd[1:]
scnd=temp.strip()

frstString=[]
scndString=[]

for i in range(0,len(frst)):
    a=frst[i]
    pos=symbols.index(a)
    number=numbers[pos]
    frstString.append(str(number))

for i in range(0,len(scnd)):
    a=scnd[i]
    pos=symbols.index(a)
    number=numbers[pos]
    b=str(number)
    scndString.append(b)

frstString=frstString[::-1]
scndString=scndString[::-1]
krat=0
finalNumberList=[]
if len(frstString)>len(scndString):
    for i in range(0,len(frstString)):
        number1=int(frstString[i])
        if (i<len(scndString)):
            number2=int(scndString[i])
            finalNumber=number1+number2
        else:
            finalNumber=number1
        if (krat>0):
            finalNumber+=krat
            krat=0
        if (finalNumber>n-1):
            krat=int(((finalNumber)/(n-1)))
            finalNumberList.append(finalNumber-n)
        else:
            finalNumberList.append(finalNumber)
else:
    for i in range(0,len(scndString)):
        number2=int(scndString[i])
        if (i<len(frstString)):
            a=i
            number1=int(frstString[a])
            finalNumber=number1+number2
        else:
            finalNumber=number2
        if (krat>0):
            finalNumber+=krat
            krat=0
        if (finalNumber>n-1):
            krat=int(((finalNumber)/(n-1)))
            finalNumberList.append(finalNumber-n)
        else:
            finalNumberList.append(finalNumber)
if (krat>0):
    finalNumberList.append(krat)

finalNumberList=finalNumberList[::-1]

addedString=""

for i in range(0,len(finalNumberList)):
    a=int(finalNumberList[i])
    pos=numbers.index(a)
    number=symbols[pos]
    addedString+=number

print(string)
print(firstAdd)
print(secondAdd)
print(addLine)
flag=True

while(flag):
    if (len(addedString)<len(firstAdd)):
        temp=" "+addedString
        addedString=temp
    else:
        flag=False

print(addedString)
