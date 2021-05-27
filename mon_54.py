#백준 n과m(?)

from itertools import *

a,b = input().split()
data = []

data = list(map(int,input().split()))

data.sort()

test = list(combinations(data,int(b)))
for i in test :
    for j in list(i) :
        print(j,end=" ")
    print()