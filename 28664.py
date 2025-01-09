n=int(input());x=[1,0,'X',9,8,7,6,5,4,3,2]
for i in range(n) :
    c=input()
    a=[int(x) for x in c[:17]]
    b=(a[0]*7+a[1]*9+a[2]*10+a[3]*5+a[4]*8+a[5]*4+a[6]*2+a[7]*1+a[8]*6+a[9]*3+a[10]*7+a[11]*9+a[12]*10+a[13]*5+a[14]*8+a[15]*4+a[16]*2)%11
    if str(x[b])==c[17] :
        print('YES')
    else :
        print('NO')
