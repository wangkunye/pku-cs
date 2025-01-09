b=input()
a=list(b)
if len(a)<7:
    print('NO')
else :
    for x in range(len(a)-6):
        if (a[x]==a[x+1]==a[x+2]==a[x+3]==a[x+4]==a[x+5]==a[x+6]):
            print('YES')
            break
    else :
        print('NO')