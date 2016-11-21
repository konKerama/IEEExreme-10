sailing=[]
testCases=int(input())

for i in range(0,testCases):
    n=int(input())
    flower=[]

    for x in range(0,n):
        flower.append(x+1)
    flag2=True
    flag=False
    k=0

    while (flag2):
        if flag==False:
            flag=True
            number=flower[k]
            flower.append(number)
            k+=1
        else:
            flag=False
            k+=1
        if(flower[k-1]==flower[k-3]):
            flag2=False
            sailing.append(flower[k])

for x in range(0,testCases):
    print(sailing[x])
