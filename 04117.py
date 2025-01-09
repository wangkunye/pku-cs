while True:
    try :
        n=int(input())
        dp=[[0]*(n+1) for i in range(n+1)]
        for i in range(n+1):
            dp[i][1]=1
            dp[0][i]=1
        for i in range(1,n+1) :
            for j in range(2,n+1) :
                if i>=j :
                    dp[i][j]=dp[i][j-1]+dp[i-j][j]
                else :
                    dp[i][j]=dp[i][j-1]
        print(dp[n][n])
    except EOFError :
        break