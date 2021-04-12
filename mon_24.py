
def solution(record):
    answer = []
    data = []
    chk_list = {}
    for i in record:
        temp = list(i.split())
        if temp[0] == 'Enter':
            data.append([temp[1],temp[-1],'님이 들어왔습니다.'])
        elif temp[0] == 'Leave':
            data.append([temp[1], temp[-1],'님이 나갔습니다.'])
        elif temp[0] == 'Change':
            data.append([temp[1], temp[-1],'c'])

    for add in range(len(data)-1,-1,-1):
        if data[add][-1] != '님이 나갔습니다.':
            if data[add][0] not in chk_list.keys():
                chk_list[data[add][0]] = data[add][1]
    for i in data :
        if i[-1] == 'c' : continue
        answer.append(chk_list.get(i[0])+i[-1])
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))
