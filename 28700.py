def a(x) :
    s=[]
    q=x//1000;s.append('M'*q)
    x-=1000*q
    w=x//100
    if w==9 :
        s.append('CM')
    elif 5<=w<9 :
        s.append('D'+'C'*(w-5))
    elif w==4 :
        s.append('CD')
    else:
        s.append('C'*w)
    x-=100*w
    e=x//10
    if e==9:
        s.append('XC')
    elif 5<=e<9:
        s.append('L'+'X'*(e-5))
    elif e==4 :
        s.append('XL')
    else :
        s.append('X'*e)
    x-=10*e
    if x==9 :
        s.append('IX')
    elif 5<=x<9 :
        s.append('V'+'I'*(x-5))
    elif x==4 :
        s.append('IV')
    else :
        s.append('I'*x)
    return s
def b(x):
    q=w=0;h=len(x)
    while x[q]=='M' :
        w+=1000
        q+=1
        if q >= h:
            return w
    if q>=h :
        return w
    if x[q]=='C' and x[q+1]=='M' :
        w+=900
        q+=2
    if q>=h :
        return w
    if x[q]=='C' and x[q+1]=='D' :
        w+=400
        q+=2
    if q>=h :
        return w
    if x[q]=='D' :
        w+=500
        q+=1
    if q>=h :
        return w
    while x[q]=='C' :
        w+=100
        q+=1
    if q>=h :
        return w
    if x[q]=='X' and x[q+1]=='C' :
        w+=90
        q+=2
    if q>=h :
        return w
    if x[q]=='X' and x[q+1]=='L' :
        w+=40
        q+=2
    if q>=h :
        return w
    if x[q]=='L' :
        w+=50
        q+=1
    if q>=h :
        return w
    while x[q]=='X' :
        w+=10
        q+=1
    if q>=h :
        return w
    if x[q]=='I' and x[q+1]=='X' :
        w+=9
        q+=2
    if q>=h :
        return w
    if x[q]=='I' and x[q+1]=='V' :
        w+=4
        q+=2
    if q>=h :
        return w
    if x[q]=='V' :
        w+=5
        q+=1
    if q>=h :
        return w
    while x[q]=='I' :
        w+=1
        q+=1
        if q >= h:
            return w
    return w
n=input()
if n.isdigit():
    pku=a(int(n))
    for i in pku:
        print(i,end='')
else :
    print(b(n))





def arabic_to_roman(num):
    mapping = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    roman_numeral = ''
    for value, numeral in mapping:
        while num >= value:
            roman_numeral += numeral
            num -= value
    return roman_numeral

def roman_to_arabic(s):
    mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    for char in s:
        value = mapping[char]
        if value > prev_value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value
    return total

# 主程序逻辑
n = input()
if n.isdigit():
    print(arabic_to_roman(int(n)))
else:
    try:
        print(roman_to_arabic(n))
    except KeyError:
        print()