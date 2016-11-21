string=input()
b=string.split(" ",2)
a=int(b[0])
p=int(b[1])
threadsNumber=[]
threadsIndex=[]
line=[]
temp=a
for i in range(0,p):
    post=int(input())
    if post in threadsIndex:
        pos=threadsIndex.index(post)
        threadsNumber[pos]+=1
    else:
        threadsIndex.append(post)
        threadsNumber.append(1)
for (i in range(0,len(threadsIndex))):
    number=threadsNumber[i]
    if number<a:
        temp =temp-number
    else:
