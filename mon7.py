#자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = 0
    list = []
    a = 1
    while n > 0:
        list.append(n % 3)
        n = n // 3
    for i in range(len(list)-1,-1,-1):
        answer = answer + (list[i] * a)
        a = a * 3



    return answer

print(solution(45))