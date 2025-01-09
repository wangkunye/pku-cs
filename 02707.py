n=int(input())
for i in range(n):
    a,b,c=map(float,input().split())
    if b==0 :
        b=-0
    d=((b**2-4*a*c)**0.5)/(2*a);e=-b/(2*a);f=b**2-4*a*c
    if f==0 :
        print('x1=x2=%.5f'%e)
    if f>0 :
        print('x1=%.5f;x2=%.5f'%(e+d,e-d))
    else :
        print('x1=%.5f+%.5f'%(e,(-f)**0.5/(2*a))+'i;'+'x2=%.5f-%.5f'%(e,(-f)**0.5/(2*a))+'i')