a=list(input().lower())
num=1
for i in range(len(a)-1):
    if a[i]==a[i+1] :
        num+=1
    else :
        print(f'({a[i]},{num})',end='')
        num=1
        continue
print(f'({a[-1]},{num})')