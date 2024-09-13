n,k=map(int,input().split())
score=[int(x) for x in input().split()]
num=0
for i in score:
    if i>=score[k-1] and i>0:
        num+=1
print(num)