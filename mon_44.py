#프로그래머스 네트워크
def solution(n, computers):
    answer = 0
    network = [i for i in range(n)]
    visited = [0] * n
    num = 0

    def dfs(now):
        if visited[now] == 1: return 0
        visited[now] = 1
        for i in range(len(computers[now])):
            if i != now and computers[now][i] == 1:
                network[i] = min(network[i], network[now])
                dfs(i)

    for i in range(n):
        dfs(i)
    answer = len(set(network))
    print(answer)
    return answer
solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])