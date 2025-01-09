while True:
    try:
        a=input()
        if a.count('@')!=1 or a[0]=='@' or a[-1]=='@' or a[0]=='.' or a[-1]=='.' or '.' not in a :
            print('NO')
        else :
            b=a[a.index('@')-1:]
            if b[0]=='.' or '.' not in b or b[2]=='.' :
                print('NO')
            else :
                print('YES')
    except EOFError:
        break
