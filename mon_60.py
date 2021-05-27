#  이코테 5

from itertools import *

a, b = map(int,input().split())

data = list(map(int,input().split()))

data.sort()
anw = 0
print(list(combinations(data,2)))
print(len(list(combinations(data,2))))