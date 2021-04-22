# 완전탐색/ 모의고사

def solution(answers):
    answer = []
    case_1 = [1,2,3,4,5]
    case_2 = [2,1,2,3,2,4,2,5]
    case_3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0] * 3
    for i in range(len(answers)) :
        if answers[i] == case_1[i%5]:
            score[0] += 1
        if answers[i] == case_2[i%8]:
            score[1] += 1
        if answers[i] == case_3[i%10]:
            score[2] += 1
    tem = max(score)
    for i in range(len(score)):
        if tem == score[i] :
            answer.append(i+1)
    return answer

solution([1,3,2,4,2])