a=int(input())
s=input()
num = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        num += 1
print(num)
