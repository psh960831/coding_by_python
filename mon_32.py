#프로그래머스 / 스택 큐/ 기능개발
def solution(progresses, speeds):
    answer = []
    data = []
    for tem in range(len(progresses)):
        add = 100 - progresses[tem]
        if add % speeds[tem] == 0:
            data.append(int(add / speeds[tem]))
        else:
            data.append(int(add / speeds[tem]) + 1)
    print(data)
    temp = data[0]
    cnt = 1
    data = data[1:]
    for add in data:
        if temp < add:
            temp = add
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1
    answer.append(cnt)

    return answer