# 이코테 그리디 3

a = input()

start = a[0]
cnt = 0
for i in range(1,len(a)):
    if a[i] == start :
        continue
    else :
        start = a[i]
        cnt += 1
print(cnt-1)
