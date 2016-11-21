string=input()
myString=string.split(" ",3)
c=int(myString[0])
h=int(myString[1])
o=int(myString[2])
w=(1/4)*h+(1/2)*o+(-1)*c
g=(1/24)*h+(-1/12)*o+(1/6)*c
carb=(-1/4)*h+(1/2)*o
intw=int(w)
intg=int(g)
intcarb=int(carb)
if (w==intw) and (g==intg) and (carb==intcarb):
    print (int(w),int(carb),int(g))
else:
    print("Error")
