a=list(input())
b=[chr(x) for x in range(ord('A'),ord('Z')+1)]
c=[chr(x) for x in range(ord('a'),ord('z')+1)]
for i in range(0,len(a)):
    if a[i] in b:
        a[i]=a[i].lower()
    elif a[i] in c:
        a[i]=a[i].upper()
print(''.join(a))