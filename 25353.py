from collections import deque

n, d = map(int, input().split())
h = deque(int(input()) for _ in range(n))
ans = []

while h:
    inlist = []
    max_val = h[0]
    min_val = h[0]

    # 一次遍历完成所有必要的计算
    for _ in range(len(h)):
        height = h.popleft()
        if abs(height - max_val) <= d and abs(height - min_val) <= d:
            inlist.append(height)
        else:
            h.append(height)

        if height < min_val:
            min_val = height
        if height > max_val:
            max_val = height

    ans += sorted(inlist)

print(*ans, sep='\n')