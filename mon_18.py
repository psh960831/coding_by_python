from itertools import combinations


def solution(orders, course):
    answer = []
    for num in range(len(course)):
        list = []
        anw_dic = {}
        for j in range(len(orders)) :
    # stirng에서도  sorted를 통해 정렬을 진행할 수 있다.
   #         anw_dic = {}
   #         for j in range(len(orders)):
   #             chang = []
   #             for k in range(len(orders[j])):
   #                 chang.append(orders[j][k])
   #             chang.sort()
   #             orders[j] = (''.join(chang))
            for i in combinations(sorted(orders[j]),course[num]):
                list.append(''.join(i))
        for i in list:
            try:
                anw_dic[i] += 1
            except:
                anw_dic[i] = 1
        res = sorted(anw_dic.items(),key=(lambda x:x[1]),reverse=True)
        if len(res) < 1 :continue
        if res[0][1] < 2: continue
        answer.append(res[0][0])
        for j in range(1,len(res)) :
            if res[j][1] == res[0][1] :
                answer.append(res[j][0])
            else : break
        answer.sort()
    return answer

a =["XYZ", "XWY", "WXA"]
b =[2,3,4]
print(solution(a,b))
""" 연습해보자!
from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        counter = Counter(temp)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]

    return sorted(answer)
"""