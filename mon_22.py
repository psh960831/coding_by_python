def solution(info, query):
    answer = []
    data = []
    want = []
    for i in info :
        data.append(list(i.split(" ")))
    for i in query :
        i = i.replace(" and "," ")
        want.append(list(i.split(" ")))
    data = sorted(data,key=lambda x:int(x[-1]),reverse=True)
    for i in want :
        lan = i[0]
        roll = i[1]
        exp = i[2]
        pre = i[3]
        num = i[4]
        cnt = 0
        for j in data :
            if int(j[4]) < int(num):
                break
            if j[0] != lan:
                if lan != '-':
                    continue
            if j[1] != roll:
                if roll != '-':
                    continue
            if j[2] != exp:
                if exp != '-':
                    continue
            if j[3] != pre:
                if pre != '-':
                    continue
            cnt += 1
        answer.append(cnt)
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))