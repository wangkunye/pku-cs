n=int(input());out=0
for x in range(n):
    a,b,c=map(int,input().split())
    if a+b+c>1:
        out+=1
print(out)
