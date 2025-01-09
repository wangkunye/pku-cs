b=list(input())
a=[]
c=[]
e=0
for i in b:
    if i==',' :
        continue
    else :
        s=int(i)
        if s<0 :
            if e>0 :
                c.append(e)
                e=0
            c.append(s)
        else :
            e+=s
if e>0 :
    c.append(e)
