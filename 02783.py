while True:
    t = int(input())
    a = []
    for i in range(t):
        x, y = map(int, input().split());b=0
        for k in range(len(a)):
            if x >= a[k][0] and y > a[k][1] or x > a[k][0] and y >= a[k][1]:
                b=1
                break
        if b==0 :
            a.append([x,y])
    print(len(a))


