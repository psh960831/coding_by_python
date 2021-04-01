def solution(board, moves):
    answer = 0
    stack = [0]
    for i in moves:
        for b in board:
            if b[i-1] != 0:
                if stack[-1] == b[i-1]:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(b[i-1])
                b[i-1] = 0
                break
    return answer