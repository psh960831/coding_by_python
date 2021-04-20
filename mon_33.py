from queue import PriorityQueue
from collections import deque
que = PriorityQueue()
def solution1(priorities, location):
    answer = 0
    data = [0] * len(priorities)
    num = 1
    while True :
        if data[location] != 0 :
            break
        for i in range(len(priorities)):
            chk = 1
            if data[i] != 0 : continue
            for j in range(len(priorities)):
                if j==i : continue
                if priorities[i] < priorities[j] :
                    chk = 0
                    break
            if chk :
                data[i] = num
                priorities[i] = 0
                num += 1
    answer = data[location]
    return answer


def solution2(priorities, location):
    answer = 0

    d = deque([(v,i) for i,v in enumerate(priorities)])
    print(d)
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


#solution1([1, 1, 9, 1, 1, 1],0)
solution2([1, 1, 9, 1, 1, 1],0)