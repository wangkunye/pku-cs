a=input().lower()
for i in a[:] :
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y':
        a=a.replace(i,'')
print('.',end='');print('.'.join(a))