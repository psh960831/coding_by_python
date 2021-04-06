a = "aabbaccc"

# 복습하자 카카오 2020 문자열 압축문제!
def solution(s):
    anw_list = []
    for cut in range(1,len(s)):
        add = ""
        split = [s[i:i+cut]for i in range(0,len(s),cut)]
        cnt = 1
        for j in range(1,len(split)):
            now,next = split[j-1],split[j]
            if now == next :
                cnt += 1
            else :
                add += (str(cnt)+now) if cnt > 1 else now
                cnt = 1

        add += (str(cnt)+split[-1] if cnt > 1 else split[-1])
        anw_list.append(len(add))


    return min(anw_list)

print(solution(a))