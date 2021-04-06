#다이나믹 내답안
n,m = map(int,input().split())
data = []
all_data = [-1]*10001
for i in range(n):
    data.append(int(input()))
    all_data[data[-1]] = 1
data.sort()


for want in range(data[0],m+1) :
    for i in data :
        if all_data[want-i] != -1 :
            add = all_data[want-i]+1
            if all_data[want] == -1 :
                all_data[want] = add
            else :
                all_data[want] = min(add,all_data[want])
print(all_data[m])
# 정규답안
"""
d = [1001]*(m+1)

d[0] = 0
for i in range(n):
    for j in range(data[i],m+1):
        if d[j-data[i]] != 1001 :
            d[j] = min(d[j],d[j-data[i]]+1)
if d[m] == 1001 :
    print(-1)
else :
    print(d[m])
"""