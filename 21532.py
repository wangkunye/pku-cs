a=int(input())
for i in range(6,a):
    if a%i==0:
        b=i
        break
print(int(a/i))






a=int(input());b=6
while a%b!=0:
    b+=1
print(int(a/b))