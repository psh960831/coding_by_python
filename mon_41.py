def solution(n, costs):
    answer = 0
    visit = [0] * n
    costs.sort(key=lambda x:x[2])
    routes = [costs[0][0]]
    while len(routes) < n :
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes :
                continue
            if cost[0] in routes or cost[1] in routes :
                routes.append([cost[0],cost[1]])
                answer += cost[2]
                costs[i] = [-1,-1,-1]
                break
        print(routes)
    print(routes)
    return answer

def solution2(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key = lambda x: x[2]) # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]]) # 집합
    while len(routes)!=n:
        for i, cost in enumerate(costs):
            if cost[0] in routes and cost[1] in routes:
                continue
            if cost[0] in routes or cost[1] in routes:
                routes.update([cost[0], cost[1]])
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
        print(routes)
    print(ans)
    return ans



solution2(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])