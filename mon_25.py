a = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
move = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def solution(maps):
    answer = 0
    data = [[10001] * len(maps[0]) for i in range(len(maps))] #
    visit = [[0]*len(maps[0]) for i in range(len(maps))]
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    def bfs(x,y,num) :
        if len(maps)<= y or y < 0 or len(maps[0]) <=x or x < 0 : return 0
        if data[x][y] > num: visit[x][y] = 0
        if maps[x][y] == 0 or visit[x][y] == 1 : return 0
        visit[x][y] = 1
        data[x][y] = min(data[x][y],num)
        for i in range(4):
            bfs(x+move[i][0],y+move[i][1],data[x][y]+1)
    bfs(0,0,1)
    answer = data[-1][-1]
    if answer == 10001 : return -1

    return answer


print(solution(a))