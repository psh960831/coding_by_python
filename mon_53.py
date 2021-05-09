# 카카오 2021 코테 3번
def solution(n, k, cmd):
    answer = ''
    deledted = []
    now = k
    max = n

    for i in cmd :# 명령어
        if i[0] == "D" :
            temp = i.split(" ")
            now = now + int(temp[-1])
        elif i[0] == "U" :
            temp = i.split(" ")
            now = now - int(temp[-1])
        elif i[0] == "C" :
            tem = 0
            for j in deledted:
                if j <= now :
                    tem+=1
            deledted.append(now+tem)
            max -= 1
            if now > max :
                now -= 1
        elif i[0] == "Z" :
            deledted.pop()
            max += 1

    for i in range(n) :
        if i in deledted :
            answer += "X"
        else :
            answer += "O"
    return answer

solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])