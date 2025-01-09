ha={'pop':0, 'no':1, 'zip':2, 'zotz':3, 'tzec':4, 'xul':5, 'yoxkin':6, 'mol':7, 'chen':8, 'yax':9, 'zac':10, 'ceh':11, 'mac':12, 'kankin':13, 'muan':14, 'pax':15, 'koyab':16, 'cumhu':17,'uayet':18}
tz=['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']
n=int(input());end=[]
for i in range(n):
    x,y,z=input().split()
    x=int(x[:x.index('.')])+1
    y=ha[y]
    z=int(z)
    s=x+y*20+z*365
    q=s//260
    s-=260*q
    if s==0 :
        q-=1
    w=s%20-1;e=s%13
    if e==0 :
        e=13
    end.append(f'{e} {tz[w]} {q}')
print(n)
print('\n'.join(end))
