f=open("perepis.txt", "r")
z=0
for i in f:
    L=i.split()
    if int((L[3][-2:]))<78:
        print(L[1],L[2])
        z=z+1
print(z)







