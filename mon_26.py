from itertools import combinations


def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])

    temp = []
    for i in range(1, col + 1):
        temp.extend(combinations(range(col), i))
    print(temp)
    unique = []
    for tem in temp:
        uni = [tuple([item[i] for i in tem]) for item in relation]
        if len(set(uni)) == row:
            unique.append(tem)

    answer = set(unique)
    print(unique)
    print(answer)
    for i in range(len(unique)):
        for j in range(i + 1, len(unique)):
            if len(unique[i]) == len(set(unique[i]) & set(unique[j])):
                answer.discard(unique[j])

    return len(answer)

    return answer

a = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(a)