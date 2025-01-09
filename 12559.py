import functools
def jk(x,y) :
    return int(y+x)-int(x+y)
n=int(input())
a=list(input().split())
a.sort(key=functools.cmp_to_key(jk))
q=int(''.join(a))
w=int(''.join(a[::-1]))
print(q,w)
