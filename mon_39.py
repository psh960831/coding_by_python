# 프로그래머스 / 그리디 / 조이스틱

def solution(name):
    answer = 0
    now = 0
    visited = [0] * len(name)
    data = [i for i in name]
    right = 1
    left = 1
    while right < len(name) :
        visited[now] = 1
        answer += min(ord(data[now])-ord('A'),(ord('Z')+1)-ord(data[now]))
        #print("add :",min(abs(ord(data[now])-ord('A')),abs(ord('X')+1-ord(data[now]))))
        while right < len(name) :
            if data[(now+right)%len(name)] != 'A' and visited[(now+right)%len(name)] != 1 :
                now = (now+right)%len(name)
                answer += right
                #print(visited, answer, right, "R")
                break
            if data[(now-left)%len(data)] != 'A' and visited[(now-left)%len(data)] != 1 :
                now = (now-left)%len(data)
                answer += left
                #print(visited, answer, left, "L")
                break
            right += 1
            left += 1

    return answer

print(solution("BBBAAAB")) # 0 1 2 3 4 5 = 15