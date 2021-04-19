# 프로그래머스 / 해시 / 위장
from itertools import *

def solution(clothes):
    answer = 1
    data = {}
    for i in clothes :
        if i[1] in data :
            tem = i[1]
            data[tem] += 1
        else :
            data[i[1]] = 2

    for add in data :
        answer = answer*data[add]
    answer -= 1

    return answer
a = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(a))