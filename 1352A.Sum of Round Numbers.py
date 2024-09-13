t=int(input())
for i in range(t):
    n=[int(x) for x in reversed(input())]
    num=0
    for k in n:
        if k!=0:
            num+=1
    print(num)
    for k in range(len(n)):
        if n[k]!=0:
            print(n[k]*(10**k),end=' ')
    print()



