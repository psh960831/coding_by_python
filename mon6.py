def solution(n, lost, reserve):
    answer = 0
    answer += n - len(lost)

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                reserve[j] = -1
                lost[i] = -5
                answer += 1

    for i in lost:
        for j in range(len(reserve)):
            if i + 1 == reserve[j] or i - 1 == reserve[j]:
                reserve[j] = -1
                answer += 1

    if answer > n: answer = n
    return answer