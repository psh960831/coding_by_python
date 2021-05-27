#이코테 그리디 1
data = list(map(int,input().split()))

data.sort()

anw = 0
cnt = 0

for i in data :
    cnt += 1
    if cnt >= i :
        anw += 1
        cnt = 0
print(anw)