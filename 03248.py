try :
    while True:
        j,k=map(int,input().split());c=[]
        for i in range(1,min(j,k)+1) :
            if j%i==0 and k%i==0 :
                c.append(i)
        print(max(c))
except EOFError:
    pass