s=input();a=b=c=d=0
for i in s:
    if i!='h' or 'e' or 'l' or 'o' :
        s=s.replace(i,'')
    if i=='h' and a<2 :
        a+=1
    else :
        s=s.replace(i,'')
    if i=='e' and b<2 :
        b+=1
    else :
        s=s.replace(i,'')
    if i=='l' and c<3 :
        c+=1
    else :
        s=s.replace(i,'')
    if i=='o' and d<2 :
        d+=1
    else :
        s=s.replace(i,'')
if s=='hello' :
    print('YES')
else :
    print('NO')
print(s)