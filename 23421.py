import math


def fn(i, s):

  if (s < 0):
    return -math.inf
  if (i == len(v)):
      return 0

  return max(fn(i+1, s), v[i] + fn(i+1, s-w[i]))


N, B = map(int, input().split())
*v, = map(int, input().split())
*w, = map(int, input().split())
print(fn(0, B))
