import heapq


def solution(tickets):
    answer = ["ICN"]
    start = "ICN"
    data = {}
    for i in tickets:
        if i[0] not in data:
            data[i[0]] = [i[1]]
        elif i[0] in data:
            data[i[0]].append(i[1])
    for i in data.values() :
        i.sort()

    while True :
        print(answer,data)
        if len(answer) == len(tickets)+1 : break
        for i in data[start] :
            answer.append(i)
            data[start].remove(i)
            start = i
            break

    print(answer)

    return answer




solution([['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']])