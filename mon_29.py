#프로그래머스 / 해시 / 베스트앨범

def solution(genres, plays):
    answer = []
    data = {}
    data_sum = {}
    for add in range(len(genres)) :
        if genres[add] in data :
            data[genres[add]].append([plays[add],add])
            data_sum[genres[add]] += plays[add]
        else :
            data[genres[add]] = []
            data[genres[add]].append([plays[add],add])
            data_sum[genres[add]] = plays[add]
    data_sum = sorted(data_sum.items(),key=lambda x:x[1],reverse=True)
    for chk in data_sum :
        temp = sorted(data[chk[0]],key = lambda x:x[0],reverse=True)[:2]
        for tem in temp :
            answer.append(tem[1])

    return answer


a = ["classic", "pop", "classic", "classic"]
b = [150, 600, 250, 250]
print(solution(a,b))