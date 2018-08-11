import random


def matching(a,b):
    num = 0
    if len(a) == len(b) or len(a) < len(b):
        for i in range(0, len(a)):
            if a[i] == b[i]:
                num = num + 1
    else:
        for i in range(0,len(b)):
            if a[i] == b[i]:
                num = num + 1
    return num


def stringToList(s):
    i = 0
    l = []
    while i < len(s):
        l.append(s[i])
        i = i + 1
    return l

def noDupeMatch(a,b):
    num = 0
    l = []
    if len(a) == len(b) or len(a) < len(b):
        for i in range(0,len(a)):
            if a[i] in b and a[i] not in l:
                num = num+1
                l.append(a[i])
    else:
        for i in range(0,len(b)):
            if b[i] in a and b[i] not in l:
                num = num+1
                l.append(b[i])
    return num
                        


a = [1,2,3]
b = [1,3,4]

c = [2,2,5]
d = [1,2,4,5,6]
e = [3,3,3,3]

print matching(a,b)
print matching(a,c)
print matching(d,a)

hi = "Hoooot"
print stringToList(hi)

print noDupeMatch(a,b)
print noDupeMatch(a,c)
