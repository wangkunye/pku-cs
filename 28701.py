
n,k=map(int,input().split())
a= list(map(int, input().split()))
a.sort()
s = sum(a)
while True:
    if a[-1] > s / k:
        b=a.pop()
        s -=b
        k -= 1
    else:
        print(f'%.3f'%(s/k))
        break