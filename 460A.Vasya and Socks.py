n,m = map(int, input().split())
t = n
while t//m>0:
        n += t//m
        t = t//m + t%m
print(n)
