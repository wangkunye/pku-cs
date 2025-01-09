from bisect import bisect_right
def min_testers_needed(scores):
    scores.reverse()
    lis = []
    for score in scores:
        pos = bisect_right(lis, score)
        if pos < len(lis):
            lis[pos] = score
        else:
            lis.append(score)

    return len(lis)
N = int(input())
scores = list(map(int, input().split()))

result = min_testers_needed(scores)
print(result)