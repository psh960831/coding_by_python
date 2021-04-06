# 다이나믹
num = int(input())
list = [0]*30001
# 5*5,5*3,5*2,3*3,3*2,2*2, 5 -1 , 3-1, 2 -1
for i in range(2,num) :
    list[i] = list[i]+1
    if list[i] % 2 == 0:
        list[i] = min(list[i]+1,list[i]//2+1)
    if list[i] % 3 == 0:
        list[i] = min(list[i]+1,list[i]//3+1)
    if list[i] % 5 == 0:
        list[i] = min(list[i]+1,list[i]//5+1)

print(list[num-1])





