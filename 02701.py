n=int(input())
b=list(range(1,n+1))
for i in b:
    if i%7==0 or '7' in str(i) :
        b.remove(i)
        print(b)
c=0
for i in b:
    c+=i**2
print(c)



