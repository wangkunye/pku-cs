n=int(input())
a=n//100
n-=100*a
b=n//20
n-=20*b
c=n//10
n-=10*c
d=n//5
n-=5*d
print(a+b+c+d+n)