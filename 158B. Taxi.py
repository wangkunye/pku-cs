import bisect
from bisect import bisect_right
import math
n=int(input())
a=list(map(int,input().split()))
a.sort()
q=bisect_right(a,1)
w=bisect_right(a,2)-q
e=bisect_right(a,3)-q-w
f=n-q-w
if e>=q :
    print(f+math.ceil(w/2))
else :
    q-=e
    if q>=2*w :
        print(f+w+math.ceil((q-2*w)/4))
    else :
        w-=math.ceil(q/2)
        print(f+math.ceil(q/2)+math.ceil(w/2))