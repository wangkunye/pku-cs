n=int(input());a=[4,7,47,74,447,477,474,774,744,747];b=0
for i in a:
    if n%i==0:
        print('YES')
        break
    else :
        b+=1
if b==10 :
    print('NO')