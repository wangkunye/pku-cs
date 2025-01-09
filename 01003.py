while True:
    a=float(input());b=0;c=2
    if a>0:
        while b<a:
            b+=(1/c)
            c+=1
        print(c-2,end=' ');print('card(s)')
    if a==0.00:
        break