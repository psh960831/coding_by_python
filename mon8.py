from collections import deque
n ,m = map(int,input().split())
miro = []

for i in range(n) :
    miro.append(list(map(int,input())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(x1,y1) :
    queue = deque()
    queue.append((x1,y1))

    while queue :
        print(queue)
        x, y = queue.popleft()
        print(queue)
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx,ny)
            if nx <0 or nx >= n or ny <0 or ny >= m :
                continue

            if miro[nx][ny] == 0 :
                continue

            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x1][y1] +1
                print(miro)
                queue.append((nx,ny))
                print(queue)

        return miro[n-1][m-1]

print(bfs(0,0))



