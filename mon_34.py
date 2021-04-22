# 프로그래머스 힙 스코빌지수맞추기

import heapq as hq

def solution(scoville, K):
    hq.heapify(scoville)
    answer = 0
    while True :
        first = hq.heappop(scoville)
        if first >= K :
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville,first+second*2)
        answer+=1


solution([1, 2, 3, 9, 10, 12],7)