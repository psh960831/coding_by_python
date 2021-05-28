#이코테 11

n = eval(input()) # 크기
cnt_1 = eval(input()) # 사과갯수
apple = []
for i in range(cnt_1) :
    apple.append(list(map(int,input().split())))
cnt_2 = eval(input()) # 움직인갯수
move = []
for i in range(cnt_2) :
    move.append(list(map(str,input().split())))
snake = [[1,1]]
time = 0

dist = [[0,1],[1,0],[0,-1],[-1,0]]

now = 0


while True :
    print(snake, now, time)
    time += 1
    next_y = snake[-1][0]+dist[now][0]
    next_x = snake[-1][1]+dist[now][1]
    if next_x > n or next_y > n or next_x < 1 or next_y < 1 :
        print(time)
        print("@@")
        break
    add = [next_y,next_x]
    if add in snake :
        print(time)
        print("!!", add)
        break
    snake.append(add)
    if add in apple :
        apple.remove(add)
    else :
        snake = snake[1:]
    for i in move :
        if int(i[0]) == time :
            if i[1] == 'D' :
                now += 1
                if now > 4 :
                    now = 0
            else :
                now -= 1
                if now < 0 :
                    now = 3
        elif int(i[0]) > time :
            break


