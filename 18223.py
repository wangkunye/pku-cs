m=int(input())
for i in range(m):
    nm='NO'
    a,b,c,d=map(int,input().split())
    for i in [a,-a]:
        for q in [b,-b]:
            for j in [c,-c]:
                for k in [d,-d]:
                    if i+q+j+k==24:
                        nm="YES"
    print(nm)