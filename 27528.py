from collections import deque

def bfs(n) :
    ans=1
    q=deque()
    for i in range(n,0,-1) :
        q.append(i)
    while q :
        a=q.popleft()
        for i in range(n-a,0,-1) :
            q.append(a+i)
            if a+i==n :
                ans+=1
    return ans

print(bfs(int(input())))
