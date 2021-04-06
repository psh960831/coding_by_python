num = int(input())
data = list(map(int,input().split()))
chk = [0]*num
answer = 0
for i in range(len(data)) :
    for j in range(i,len(data)) :
        chk[i] += 1 if data[i] < data[j] else 0
answer = num - chk.count(0)

print(answer)

data.reveser()

dp = [1]*num
for i in range(1,num):
    for j in range(0, i):
        if data[j]<data[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(num-max(dp))