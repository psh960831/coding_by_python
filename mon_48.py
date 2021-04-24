from itertools import *


def solution(a):
    answer = 0
    cnt = len(a) // 2
    for i in range(cnt, 1, -1):
        temp = list(combinations(a, 2 * i))
        for j in temp:
            tem = list(j)
            data = [0] * (10)
            for j in range(0,len(tem), 2):
                if tem[j] == tem[j + 1]:
                    break
                data[tem[j]] += 1
                data[tem[j + 1]] += 1
            if not (len(tem)//2) in data:
                continue
            return len(tem)
    return answer

print(solution(	[0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))