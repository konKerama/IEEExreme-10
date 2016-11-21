t=int(input())
sOGroup=[1.880,1.023,0.729,0.577,0.483,0.419,0.373,0.337,0.308]
for i in range(0,t):
    string=input()
    x=int(string[0:2])
    a=string.split(" ",x+2)
    n=int(a[1])
    v=[]
    a2=sOGroup[n-2]
    for y in range(0,x):
        v.append(a[y+2])
    xav=[]
    subRange=[]
    for k in range(0,n):
        s=0
        op=k*n
        minEl=int(v[op])
        maxEl=int(v[op])
        g1 = int(k*n)
        g2 = int((k+1)*n)
        for l in range(g1,g2):
            s+=int(v[l])
            if int(v[l])<int(minEl):
                minEl=v[l]
            if int(v[l])>int(maxEl):
                maxEl=v[l]
        av=s/n
        xav.append(av)
        sRange=int(maxEl)-int(minEl)
        subRange.append(sRange)
    sAv=float(0)
    sRang=0
    for k in range(0,len(xav)):
        sAv=sAv+float(xav[k])
        sRang+=subRange[k]
    average=sAv/len(xav)
    avRanges=sRang/len(xav)

    uclx=average+a2*avRanges
    ucly=average-a2*avRanges
    clx=average
    sigma=(uclx-average)/3

    flag1=False
    for w in range(0,x):
        if (int(v[w])>uclx) or (int(v[w])<ucly):
            flag1=True

    flag2=False
    if (not flag1):
        for w in range(0,x-2):
            if (v[x]>average+2*sigma) and ((v[x+1]>average+2*sigma)or(v[x+2]>average+2*sigma)):
                flag2=True
            if (v[x]<average-2*sigma) and ((v[x+1]<average-2*sigma)or(v[x+2]<average-2*sigma)):
                flag2=True

    flag3=False
    if (not flag1)and (not flag2):
        for w in range(0,x-5):
            counter1=0
            counter2=0
            for q in range(0,5):
                if v[q]>average+sigma:
                    counter1+=1
                elif v[q]<average-sigma:
                    counter2+=1
            if (v[x]>average+sigma) and (counter1>=4):
                flag3=True
            elif (v[x]<average-sigma) and (counter2>=4):
                flag3=True

    flag4=False
    if (not flag1)and (not flag2) and (not flag3):
        for w in range(0,x-8):
            counter1=0
            counter2=0
            for q in range(0,8):
                if v[q]>average:
                    counter1+=1
                elif v[q]<average:
                    counter2+=1
            if (v[x]>average) and (counter1==8):
                flag4=True
            elif (v[x]<average) and (counter2==8):
                flag4=True
    if (flag1)or (flag2)or (flag3)or (flag4):
        print("Out of Control")
