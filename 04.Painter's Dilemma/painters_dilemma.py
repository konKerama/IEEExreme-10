
#LIMITATIONS t(1,5) n(1,500) ci(1,20)
import math

t = int( input())
s = int(0)
counter=[]
while( s < t ):
    n = int( input())
    c = []
    j = int(0)
    string=input()
    c=string.split(" ",n-1)
    a = int(c[0])
    b = int(c[1])
    count = int(2)
    depth = 20
    future = []
    i=int(0)
    while ( i<n ):
        if( i>1 ):
            if( i + depth <= n ):
                future = c[i: i+depth]
            else:
                future = c[i: n]
            k=0
            for x in range(0,len(future)):
                if (a==int(future[x])):
                    k+=1
            l=0
            for x in range(0,len(future)):
                if (b==int(future[x])):
                    l+=1
            if k <= l:
                if a != c[i]:
                    a = c[i]
                    count += 1
            else:
                if b != c[i]:
                    b = c[i]
                    count += 1
            future = list()        
        i += 1
    s += 1
    counter.append(count)
for element in counter:
    print (element)

    
        
