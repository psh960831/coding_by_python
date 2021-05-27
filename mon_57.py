# 이코테 그리디 2
a = input()
anw = int(a[0])

for i in range(1,len(a)) :
    if a[i] == '0' or anw == 0 :
        anw += int(a[i])
    else :
        anw = anw*int(a[i])

print(anw)
