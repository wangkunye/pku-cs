s = input()
b = 0
c= [0]
for i in range(1,len(s)):
    if s[i] == s[i-1]:
        b+=1
    c.append(b)
m=int(input())
for i in range(m):
    x,y = map(int, input().split())
    print(c[y-1] - c[x-1])