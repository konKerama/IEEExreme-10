t=int(input())
output=[]
for y in range(0,t):
    limit=False
    while(not limit):
        a=input()
        n=int(a[0])
        k=int(a[2])
        if (n<100000)and(k<n):
            limit=True
    x=[]
    for i in range(0,n):
        a=i+1
        #string="Give me the size of the ",a," dog"
        w=int(input())
        x.append(w)
    x.sort()
    space=[]
    for kSpaces in range(0,k-1):
        maxl=-1000000000
        for l in range(0,n-1):
            weightDiff=int(x[l+1]-x[l])
            if ((weightDiff>maxl)and(l not in space)):
                maxl=weightDiff
                index=l
        space.append(index)
    space.sort()
    sumWeight=0
    flag=0
    for s in range(0,k):
        if (s==k-1):
            currWeight=int(x[n-1]-x[space[s-1]+1])
        else:
            currWeight=int(x[space[s]]-x[flag])
            flag=space[s]+1
        sumWeight+=currWeight
    output.append(sumWeight)
for y in range(0,t):
    print(output[y])
