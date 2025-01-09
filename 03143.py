x=int(input())
a=list(i for i in range(2,x+1))
for i in range(3,x+1):
    if i%2==0 :
        a.remove(i)
    else :
        for k in range(2,int(i**0.5)+1):
            if i%k==0:
                a.remove(i)
                break
if x<6 or x%2!=0 :
    print('Error!')
else :
    for i in a:
        if i<=x/2 and x-i in a:
             print(f'{x}={i}+{x-i}')
        else :
            continue

