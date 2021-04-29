#  프로그래머스 캐시
def solution(cacheSize, cities):
    answer = 5
    data = [i.lower() for i in cities]
    data.reverse()
    if cacheSize == 0: return 5 * len(cities)
    if len(cities) == 0: return 0
    cash = [data.pop()]

    while len(data):
        temp = data.pop()
        if temp in cash:  # 캐시에 데이터가 있는경우
            answer += 1
            cash[0], cash[cash.index(temp)] = temp, cash[0]
        elif temp not in cash:  # 캐시에 데이터가 없는경우
            if len(cash) < cacheSize:
                cash.append(temp)
            elif len(cash) >= cacheSize:
                cash.pop(0)
                cash.append(temp)
            answer += 5
    return answer