q=[[0 for k in range(1025)] for i in range(1025)]
d=int(input())
n=int(input())
for i in range(n):
    z,x,c=map(int,input().split())
    for w in range(max(0,z-d),min(1024,z+d)+1):
        for e in range(max(0,x-d),min(1024,x+d)+1):
            q[w][e]+=c
f=max(j for i in q for j in i);g=0
for o in range(1025) :
        g+=q[o].count(f)
print(g,f)