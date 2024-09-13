t=int(input())
a=[int(x) for x in input().split()]
num=0
b=0
for i in a:
    if i==-1 and b==0:
        num+=1
    else:
        b+=i
print(num)
