def solution(n, edge):
    answer = 0
    data = [20001] * (n + 1)
    visited = [0] * (n + 1)
    data[1] = 0

    def chk(now):
        for i in edge:
            if i[0] == now:
                if data[i[1]] > data[now]+1 :
                    data[i[1]] = data[now] + 1
                    chk(i[1])
            elif i[1] == now:
                if data[i[0]] > data[now] + 1:
                    data[i[0]] = data[now] + 1
                    chk(i[0])

    chk(1)
    data.remove(20001)
    answer = data.count(max(data))

    return answer


from collections import deque


def solution2(n, edge):
    routes = dict()
    for e1, e2 in edge:
        routes.setdefault(e1, []).append(e2)
        routes.setdefault(e2, []).append(e1)
    print(routes)

    q = deque([[1, 0]])  # node number, depth
    check = [-1] * (n + 1)
    while q:
        index, depth = q.popleft()
        check[index] = depth
        for i in routes[index]:
            if check[i] == -1:
                check[i] = 0
                q.append([i, depth + 1])
        depth += 1
    return check.count(max(check))


solution2(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])