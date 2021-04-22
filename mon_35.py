# 프로그래머스 / 힙 / 디스크 컨트롤러
import heapq as hq


def solution(jobs):
    answer = 0
    hq.heapify(jobs)
    now = 0
    data = [0] * len(jobs)
    while len(jobs) :
        temp = []
        for i in jobs :
            if i[0] == now :
                tem = hq.heappop(jobs)
                add = tem[1] + abs(tem[0]-now)
                answer += add
                now += add
                break
            elif i[0] < now :
                temp.append(hq.heappop(jobs))
            else :
                break







    return answer

solution([[0, 3], [1, 9], [2, 6]])