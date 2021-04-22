# 완전탐색 / 소수찾기
from itertools import*
import math
def chk(num) :
    if num == 1 or num ==  0 : return 0

    for i in range(2,int(math.sqrt(num))+1) :
        if num % i == 0 :
            return 1
    return num


def solution(numbers):
    answer = 0
    data = []
    prime_num = []

    def chk(num):
        if num == 1 or num == 0: return 0
        if num in prime_num : return 0
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return 0
        return num

    for i in numbers :
        data.append(i)

    for select in range(1,len(data)+1):
        temp = list(permutations(data,select))
        for i in temp :
            tem = int("".join(i))
            if chk(tem) :
                prime_num.append(tem)
                answer+=1

    return answer

print(solution("011"))