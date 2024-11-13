import random
N = int(input())
l=[]
a=0
while a<N:
    a+=1
    l+= [random.randint(0, 1000)]
print(l)
a = 0
i = 0
n = 0
v=1
while n < len(l) - 1:
    while i < len(l) - v:
        a = l[i]
        A = l[i + 1]
        if A > a:
            l[i] = A
            l[i + 1] = a
        i += 1
    i = 0
    n += 1
    v+=1
print(l)