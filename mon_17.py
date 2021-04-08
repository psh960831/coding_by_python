
def solution(p):
    print("-----------")
    print(p)
    if p == "" : return ""
    answer = ''
    u = ""
    v = ""
    cnt_1 = 0;
    cnt_2 = 0;
    list = []
    for i in range(len(p)):  # u찾는함수
        if p[i] == '(':
            cnt_1 += 1
            list.append(p[i])
        else:
            cnt_2 += 1
            if len(list) :
                list.pop()
        u += p[i]
        if cnt_1 == cnt_2:
            v = p[i+1:]
            break
    print(u,v)
    if len(list) == 0: #올바름
        return u + solution(v)
    else : # 올바르지 않을경우
        answer = u[1:-1]
        answer = answer.replace("(","1")
        answer =answer.replace(")","2")
        answer =answer.replace("1",")")
        answer =answer.replace("2", "(")
        return "(" + solution(v) +")" + answer

a = ")()()()("
print(solution(a))