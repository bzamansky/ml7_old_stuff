import random
#random in btwn 5&10
def random510():
    random.randint(5,10)
def ranfloat:
    random.random()*6+4.35
def matching(a,b):
    x=0
    num=0
    if len(a)==len(b) or len(a)<len(b):
        while x<len(a):
           if a[x]==b[x]: 
               num+=1
           x+=1
    if len(b)<len(a):
        while x<len(b):
            if a[x]==b[x]:
                num+=1
            x+=1
    return num

def stringToList(s):
    y=[]
    for x in s:
        y.append(x)
    return y
    
def noDupeMatch(a,b):
    x=[]
    num=0
    pos=0
    while pos<len(a):
        if a[pos] in b and a[pos]not in x:
            num+=1
            x.append(a[pos])
        pos+=1
    return num


def bargraph(a):
    line=0
    pos=0
    y=''
    while pos<len(a):
       y+= str(line)+':'+'='*a[pos]+"\n"
       line+=1
       pos+=1
    return y

def bar2(a):
    y=''
    for x in a:
        y+=str(x)
    y+='\n'

    while max(a)>0:
        pos = 0
        while pos<len(a):
            if a[pos]>0:
                y+='='
                a[pos] = a[pos] - 1
            else:
                y+=' '
            pos+=1
        y+='\n'
    return y


def randomList(num,maxi):
    y=[]
    while num>0:
        y.append(int(random.random()*maxi))
        num+= -1
    return y


def randombg():
    x=0
    while x<10:
        print bargraph(randomList(10,10))
        print bar2(randomList(10,10))         
        x+=1


print randomList(5,50)

randombg()
