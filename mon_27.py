# 프로그래머스 해시

def solution(phone_book):
        answer = True
        phone_book.sort(key=lambda x: len(x))
        print(phone_book)
        data = []
        for i in range(len(phone_book)):
            for j in data :
                temp = phone_book[i][0:len(j)]
                if temp == j : return False
            data.append(phone_book[i])
        return answer

a = ["119", "97674223", "1195524421","356"]
print(solution(a))