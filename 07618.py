from functools import cmp_to_key
def compare(x,y) :
    if x[1]>=60 and y[1]>=60 :
        if x[1]!=y[1] :
            return int(y[1])-int(x[1])
        else :
            return 0
    elif x[1]<60 and y[1]<60 :
        return 0
    else :
        return int(y[1]) - int(x[1])
n=int(input())
a=[]
for i in range(n):
    q=list(input().split())
    a.append([q[0],int(q[1])])
a.sort(key=cmp_to_key(compare))
for i in a:
    print(i[0])