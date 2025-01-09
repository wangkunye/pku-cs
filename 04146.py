from math import ceil
n=int(input())
b=3*n
while b%5!=0 :
    b-=1;
a=b-3*ceil((b-n)/3)
while (b-a)/2>n:
    b-=5
print(b)
