t=int(input())
for i in range(t):
    q=int(input());w=int(q*(q+1)/2);e=0
    while 2**e<=q :
        e+=1
    w-=(2**(e)-1)*2
    print(int(w))