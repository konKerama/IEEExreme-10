string=input()
myString=string.split(" ",3)
c=int(myString[0])
h=int(myString[1])
o=int(myString[2])
genC=7
genH=14
genO=9
flag=True
counterW=0
counterCarb=0
counterG=0
prevLen=0
oList=[]
hList=[]
cList=[]
countW=[]
countCarb=[]
countG=[]
flag=True
while (flag):
    if (c>=genC) and (h>=genH) and (o>=genO):
        #einai megalytero ta pairnw ola
        c=c-genC
        h=h-genH
        o=o-genO
        counterW+=1
        counterCarb+=1
        counterG+=1
    else:
        if (len(oList)==0):
            c2=c
            h2=h
            o2=o
            #Kanw Glikozi
            c2=c2-6
            h2=h2-12
            o2=o2-6
            if (c2>=0) and (h2>=0) and (o2>=0):
                    oList.append(o2)
                    cList.append(c2)
                    hList.append(h2)
                    a=counterG+1
                    countG.append(a)
                    counterW.append(0)
                    countCarb.append(0)
            #Kanw water
            c2=c
            h2=h
            o2=o
            h2=h2-2
            o2=o2-1
            if (c2>=0) and (h2>=0) and (o2>=0):
                    oList.append(o2)
                    cList.append(c2)
                    hList.append(h2)
                    a=counterW+1
                    countW.append(a)
                    countG.append(0)
                    countCarb.append(0)
            #Kanw Co2
            c2=c
            h2=h
            o2=o
            c2=c2-1
            o2=o2-2
            if (c2>=0) and (h2>=0) and (o2>=0):
                    oList.append(o2)
                    cList.append(c2)
                    hList.append(h2)
                    a=counterCarb+1
                    countCarb.append(a)
                    countW.append(0)
                    countG.append(0)
        else:
            for i in range (0,len(oList)):
                c2=cList[i]
                h2=hList[i]
                o2=oList[i]
                #Kanw Glikozi
                c2=c2-6
                h2=h2-12
                o2=o2-6
                if (c2>=0) and (h2>=0) and (o2>=0):
                        oList.append(o2)
                        cList.append(c2)
                        hList.append(h2)
                        a=countG[i]+1
                        countG.append(a)
                        countW.append(0)
                        countCarb.append(0)
                #Kanw water
                c2=cList[i]
                h2=hList[i]
                o2=oList[i]
                h2=h2-2
                o2=o2-1
                if (c2>=0) and (h2>=0) and (o2>=0):
                        oList.append(o2)
                        cList.append(c2)
                        hList.append(h2)
                        a=countW[i]+1
                        countW.append(a)
                        countG.append(0)
                        countCarb.append(0)
                #Kanw Co2
                c2=cList[i]
                h2=hList[i]
                o2=oList[i]
                c2=c2-1
                o2=o2-2
                if (c2>=0) and (h2>=0) and (o2>=0):
                        oList.append(o2)
                        cList.append(c2)
                        hList.append(h2)
                        a=countCarb[i]+1
                        countCarb.append(a)
                        countW.append(0)
                        countG.append(0)
    if (prevLen==len(oList)):
        flag=False
    else:
        prevLen=len(oList)

flag=True
for i in oList:
    if (oList[i]==0) and (cList[i]==0) and (hList[i]==0):
        counterW+=countW[i]
        counterG+=countG[i]
        counterCarb+=countCarb[i]
        print (counterG," ",counterCarb," ",counterW," ")
        flag=False
if (flag):
    print ("Error")
