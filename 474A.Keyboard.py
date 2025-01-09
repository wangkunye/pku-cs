x=input();y=list(input())
a=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m',',','.','/']
if x=='R' :
    for i in y:
         print(a[a.index(i)-1],end='')

else :
    for i in y:
        print(a[a.index(i)+1],end='')
        