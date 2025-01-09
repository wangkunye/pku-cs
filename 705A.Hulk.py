a=n=int(input());m=0
while n>1 :
    if m%2==0 :
        print('I hate that ',end='')
    else :
        print('I love that ',end='')
    n-=1;m+=1
print(['I love it','I hate it'][a%2])

