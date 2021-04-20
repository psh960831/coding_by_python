# 프로그래머스 / 스택 큐 / 다리를지나는 트럭-

def solution(bridge_length, weight, truck_weights):
    answer = 1
    on = []
    for tem in truck_weights:
        if not on:
            on.append(tem)
            answer += bridge_length
        elif sum(on) + tem <= weight:
            on.append(tem)
            answer += 1
        else:
            while sum(on) + tem > weight:
                on.pop(0)
            if on:
                answer -= len(on)
                
            print(on, answer)
            on = []
            on.append(tem)
            answer += bridge_length
    return answer

#print(solution(7,7,[1, 1, 1, 1, 1, 3, 3]))
print(solution(5,5,[2, 2, 2, 2, 1, 1, 1, 1, 1]))
# 22 221 111 5*3 + 1 + 2 + 2 + 1
# 2