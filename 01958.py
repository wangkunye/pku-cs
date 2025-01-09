import sys
sys.setrecursionlimit(1<<30)
def han3(n) :
    if n==1 :
        return 1
    else :
        return han3(n-1)*2+1
a=[]
for i in range(1,13):
    a.append(han3(i))
def han4(n) :
    b=[]
    for i in range(1,n+1) :
        b.append(han4(i)+a[i-1]+han4(n-i))
    return min(b)
print(han4(1))