k=int(input())
k%=26
s=input()
def genshin(x) :
    a=[]
    for i in x:
        b=ord(i)
        if 97<=b<=122:
            if b>=97+k :
                b-=k
            else :
                b-=(k-26)
        else :
            if b>=65+k :
                b-=k
            else :
                b-=(k-26)
        a.append(chr(b))
    return ''.join(a)
print(genshin(s))
