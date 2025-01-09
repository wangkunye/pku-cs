t=int(input())
num=0
for i in range(t):
    a=input()
    while '### ###' in a:
        a.replace('### ###','')
    num+=a.count('###')/2
print(int(num))