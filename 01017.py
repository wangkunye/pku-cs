import math

while True :
    a=list(map(int,input().split()))
    if sum(a)==0 :
        break
    x=a[5]
    while a[4]>0 :
        x+=1
        a[4]-=1
        if a[0]>0 :
            a[0]-=11
    while a[3]>0 :
        x+=1;y=20
        a[3]-=1
        while a[1]>0 and y>0 :
            a[1]-=1;y-=4
        while a[0]>0 and y>0 :
            a[0]-=1;y-=1
    while a[2]>=4 :
        x+=1
        a[2]-=4
    if a[2]==1 :
        x+=1
        if a[1]>=5 :
            a[1]-=5;a[0]-=7
        else :
            a[0]-=(27-4*a[1])
            a[1]=0
    if a[2]==2 :
        x+=1
        if a[1]>=3 :
            a[1]-=3;a[0]-=6
        else :
            a[0]-=(18-4*a[1])
            a[1]=0
    if a[2]==3 :
        x+=1
        if a[1]>=1 :
            a[1]-=1;a[0]-=5
        else :
            a[0]-=9

    while a[1]>=9 :
        x+=1;a[1]-=9
    if a[1]>0 :
        x+=1
        if a[0]>0 :
            a[0]-=(36-4*a[1])
    if a[0]>0 :
        import math
        x+=(math.ceil(a[0]/36))
    print(x)

