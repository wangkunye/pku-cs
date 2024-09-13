m1=[int(x) for x in input().split()]
m2=[int(x) for x in input().split()]
m3=[int(x) for x in input().split()]
m4=[int(x) for x in input().split()]
m5=[int(x) for x in input().split()]
if 1 in m1:
    print(abs(m1.index(1)-2)+2)
if 1 in m2:
    print(abs(m2.index(1)-2)+1)
if 1 in m3:
    print(abs(m3.index(1)-2))
if 1 in m4:
    print(abs(m4.index(1)-2)+1)
if 1 in m5:
    print(abs(m5.index(1)-2)+2)