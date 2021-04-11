def solution(name):
    answer = 0
    list = [min(ord(name[i])-65,91-ord(name[i])) for i in range(len(name))]
    dx = 0
    while True :
        answer += list[dx]
        list[dx] = 0
        if sum(list) == 0 :
            break
        left, right = 1, 1
        while list[dx+right] == 0:
            right += 1
        while list[dx-left] == 0:
            left += 1
        answer += left if left<right else right
        dx += -left if left < right else right

    return answer




print(solution("B"))

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z