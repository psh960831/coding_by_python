#14719
a, b = map(int,input().split())

data = list(map(int,input().split()))
visite = [data[0]]
water = 0
now_max = 0
for i in range(1,len(data)) :
    if visite[0] <= data[i] or i == len(data)-1:
        chk = min(visite[0],data[i])
        while len(visite) :
            add = max(chk - visite.pop(),0)
            water += add
        visite.append(data[i])
    else :
        visite.append(data[i])





print(water)

