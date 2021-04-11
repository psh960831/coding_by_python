n, m, c = map(int,input().split())
data = []
for i in range(m):
    add = list(map(int,input().split())) # x -> y z : 거리
    data.append(add)

dis = [1000]*(n+1)
visited = [0]*(n+1)
chk = 0
dis[c] = 0

def solution(a):
    if visited[a] != 0:
        return 0
    else :
        visited[a] = 1
    for i in range(len(data)):
        start = data[i][0]
        end = data[i][1]
        distance = data[i][2]
        if start == a :
            if dis[a] == 1000 :
                solution.chk += 1
            dis[end] = min(dis[end],dis[start]+distance)
            print(dis, distance)
            solution(end)

solution.chk = 0
solution(c)
dis.remove(1000)
print(dis)
print(max(dis))
print(visited.count(1)-1)