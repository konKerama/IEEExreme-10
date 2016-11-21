password=input()
m=int(input())
yehOrNah=[]
for x in range (0,m):
    string=input()
    myList=string.split(" ",len(string))
    defType=int(myList[0])
    if (defType==1):
        i=int(myList[1])
        j=int(myList[2])
        k=int(myList[3])
        string1=password[i:j+1]
        string2=password[k:k+j-i+1]
        if (string1==string2):
            yehOrNah.append("Y")
        else:
            yehOrNah.append("N")
    elif (defType==2):
        i=int(myList[1])
        j=int(myList[2])
        k=int(myList[3])
        string1=password[k-1:(k+j-i)]
        tempPass=password[:i-1]+string1+password[j:]
        password=tempPass
        #print(password)
    elif (defType==3):
        i=int(myList[1])
        j=int(myList[2])
        string1=password[i:j+1]
        newstr=""
        for i in range(0,len(string1)):
            if string1[i] is "z":
                newstr+="a"
            else:
                newstr+=chr(ord(string1[i])+1)
        tempPass=password[:i]+newstr+password[j+1:]
        password=tempPass
for i in range(0,len(yehOrNah)):
    print(str(yehOrNah[i]))
