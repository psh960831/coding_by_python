# 카카오 코테 2021 4번

def solution(n, start, end, roads, traps):
    answer = 0
    cost = [10001]*(n+1)
    cost[1] = 0
    visited = [0]*(n+1)
    state = True
    def find(now,now_cost,state):
        if visited[now] >= 3 : return 0
        visited[now] += 1
        cost[now] = min(cost[now], now_cost)
        if now == end :
            cost[end] = min(cost[now],now_cost)
            return 0
        if now in traps :
            state = not state
        print(cost, now , state)
        if state : # 정상/비정상 true / false
            for i in roads :
                if i[0] == now :
                    find(i[1],now_cost+i[2],state)
        else :
            for i in roads :
                if i[1] == now :
                    find(i[0],now_cost+i[2],state)

    find(start,0,state)
    print(cost)

    return answer


solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3])