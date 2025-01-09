n=int(input())
m=list(map(int,input().split()))
m.sort()
m.reverse()
a=0;b=0
for i in range(len(m)):
    if a<=sum(m)-a :
        a+=m[i]
        b+=1
    else :
        break
print(b)