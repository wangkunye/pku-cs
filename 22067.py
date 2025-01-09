a=[]
while True :
    try :
        b=input()
        if b=='pop' :
            if not a :
                continue
            a.pop()
        elif b=='min' :
            if not a :
                continue
            print(min(a))
        else :
            a.append(int(b[4:]))
    except EOFError :
        break