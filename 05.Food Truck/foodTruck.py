import math
from datetime import datetime
import sys

def compare_dates( date1, date2):
    date_1=datetime(int(date1[6:10]),int(date1[0:2]),int(date1[3:5]),int(date1[10:12]),int(date1[13:15]))
    date_2=datetime(int(date2[6:10]),int(date2[0:2]),int(date2[3:5]),int(date2[10:12]),int(date2[13:15]))
    if date_1 < date_2 :
        return True
    elif (date_1 > date_2):
        return False

rEarth=6378.178
pos=input()
listPos=pos.split(",",2)
myLatitude=float(listPos[0])
myLongtitude=float(listPos[1])
r=float(input())
header=input()
phoneNumber=[]
userTimes=[]
deletedPhones=[]
deletedPos=[]
line = sys.stdin.readline()

while(line):
    string=line
    date=string[0:10]
    time=string[11:16]
    buyerPos=string[17:len(string)]
    a=[]
    a=buyerPos.split(",",3)
    latitude=float(a[0])
    longtitude=float(a[1])
    phone=a[2]
    #print ("latitude",latitude)
    #print("longtitude",longtitude)
    #print("phone",phone)
    d=2*rEarth*math.asin(math.pi*(math.sqrt((math.sin((myLatitude-latitude)/2))**2+math.cos(myLatitude)*math.cos(latitude)*(math.sin((myLongtitude-longtitude)/2))**2))/180)
    #print (d)

    if (phone in phoneNumber):
        phonePos=phoneNumber.index(phone)
        flag=compare_dates(userTimes[phonePos],(date+time))
        if (flag):
            if (d>r):
                deletedPhones.append(phoneNumber[phonePos])
                deletedPos.append(userTimes[phonePos])
                del phoneNumber[phonePos]
                del userTimes[phonePos]
            else:
                userTimes[phonePos]=date+time
    elif (phone in deletedPhones):
        phonePos=deletedPhones.index(phone)
        flag=compare_dates(userTimes[phonePos],(date+time))
        if (flag):
            if (d<r):
                phoneNumber.append(deletedPhones[phonePos])
                userTimes.append(deletedPos[phonePos])
                del deletedPhones[phonePos]
                del deletedPos[phonePos]
            else:
                deletedPos[phonePos]=date+time
    elif (d<=r):
        phoneNumber.append(phone)
        userTimes.append(date+time)
    line = sys.stdin.readline()

stringPhoneNumber=[str(i) for i in phoneNumber]
print (",".join([str(x) for x in phoneNumber] ))
for i in range(0, len(stringPhoneNumber)):
    sys.stdout.write(stringPhoneNumber[i])
    if i != len(stringPhoneNumber)-1:
        sys.stdout.write(", ")
