# 프로그래머스 / 타켓넘버

from itertools import *

def solution(numbers, target):
    answer = 0
    all = sum(numbers)

    if all == target: return 1
    for cnt in range(1, len(numbers) + 1):  # -의 갯수
        temp = list(combinations(numbers, cnt))
        for tem in temp :
            if all - sum(tem)*2 == target :
                answer += 1

    return answer

print(solution([1, 1, 1, 1, 1],3))