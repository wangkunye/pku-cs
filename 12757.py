dic={'million':1000000,'thousand':1000,'hundred':100,'zero': 0,'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,'ten': 10,'eleven': 11,'twelve': 12,'thirteen': 13,'fourteen': 14,'fifteen': 15,'sixteen': 16,'seventeen': 17,'eighteen': 18,'nineteen': 19,'twenty': 20,'thirty': 30,'forty': 40,'fifty': 50,'sixty': 60,'seventy': 70,'eighty': 80,'ninety': 90,'negative':-1}
a=list(input().split())
b=[]
for i in a:
    b.append(dic[i])
c=0
d=0
end=0
qwe=1
for i in b:
    if i==-1:
        qwe=-1
        continue
    d=i
    if d==100 :
        c*=100
    elif d>100 :
        c*=d
        end+=c
        c=0
    else :
        c+=d
end+=c
print(qwe*end)
