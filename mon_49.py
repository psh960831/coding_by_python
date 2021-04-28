# 백준 1012번
import sys
sys.setrecursionlimit(10 ** 5)
cnt = int(input())
move_x = [0,0,1,-1]
move_y = [1,-1,0,0]

for i in range(cnt) :
    answer = 0
    m, n, k = map(int, input().split())
    data = [[0]*m for i in range(n)]
    visited = [[0]*m for i in range(n)]
    for j in range(k) :
        a, b = map(int, input().split())
        data[b][a] = 1

    if k == 1 :
        print(1)
        continue

    def dfs(n,m):
        if visited[n][m] == 1 or data[n][m] == 0 : return 0
        visited[n][m] = 1

        for i in range(4) :
            next_y = n+move_y[i]
            next_x = m+move_x[i]
            if next_x < len(data[0]) and next_x >= 0 and next_y < len(data) and next_y >=0:
                dfs(next_y,next_x)

    for y in range(n) :
        for x in range(m) :
            if visited[y][x] == 0 and data[y][x] == 1 :
                dfs(y,x)
                answer += 1

    print(answer)

