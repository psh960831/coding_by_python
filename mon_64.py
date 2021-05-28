def solution(s):
    answer = len(s)
    cut = [i for i in range(1, int(len(s) / 2)+1)]
    chk = []
    for num in cut:
        temp = ""
        data = s[:num]
        cnt = 1
        for i in range(num,len(s),num):
            if s[i:i+num] == data :
               cnt+=1
            else :
                if cnt == 1 :
                    temp += data
                    data = s[i:i+num]
                else :
                    temp = temp + str(cnt) + data
                    data = s[i:i+num]
                    cnt = 1
        if cnt == 1:
            temp = temp + data
        else :
            temp = temp + str(cnt) + data
        answer = min(answer,len(temp))
    print(answer)
    return answer


solution("ababcdcdababcdcd")