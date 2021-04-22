def solution(number, k):
    answer = ''
    data = [i for i in number]
    end = 0

    for start in range(k,len(number)) :
        print(data[start])
    return answer



print(solution("4177252841",4))