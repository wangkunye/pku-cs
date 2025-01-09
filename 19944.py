n=int(input());j=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for i in range(n):
    a=input();x=int(a[:4]);m=int(a[4:6]);d=int(a[6:8])
    if m==1 :
        m=13;x-=1
    elif m==2 :
        m=14;x-=1
    v=str(x)
    c=int(v[:2]);y=int(v[2:4])
    w=(y+y//4+c//4-2*c+(13*m+13)//5+d-1)%7
    print(j[w])
