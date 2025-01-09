import bisect

n = int(input())
a = list(map(int, input().split()))
a.sort()  # 排序数组
b = max(a)
q = int(input())

for i in range(q):
    x = int(input())

    if x >= b:  # 如果 x 大于或等于最大值，所有元素都符合条件
        print(n)
    else:
        # 使用 bisect_right 查找小于等于 x 的元素个数
        y = bisect.bisect_right(a, x)
        print(y)
