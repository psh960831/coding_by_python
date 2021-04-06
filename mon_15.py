# 다이나믹
n,m = map(int,input().split())
data = list(map(int,input().split()))
data = [data[i:i+m] for i in range(0,len(data),m)]
all = [[0]*m for i in range(n)]
print(data)
print(all)
for i in range(n) :
    all[i][0] = data[i][0]

for i in range(1,m):
    for j in range(n) :
        if j-1 < 0 : # 0보다작으니까 아래, 중간
            all[j][i] = max(all[j+1][i-1]+data[j][i],all[j][i-1]+data[j][i])
        elif j+1 >= n : # n보다 크니까
            all[j][i] = max(all[j-1][i-1]+data[j][i],all[j][i-1]+data[j][i])
        else :
            all[j][i] = max(all[j+1][i-1]+data[j][i],all[j-1][i-1] + data[j][i], all[j][i-1]+data[j][i])

print(max(map(max,all)))

