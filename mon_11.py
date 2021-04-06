def solution(numbers, hand):
    answer = ''
    list = [[4,2],[1,1],[1,2],[1,3],[2,1],[2,2],[2,3],[3,1],[3,2],[3,3]]
    # 0 1 2 3 4 5 6 7 8 9
    left = [4,1]
    right = [4,3]

    for i in numbers :
        if i in [1, 4 ,7] :
            answer += "L"
            left[0] = list[i][0]
            left[1] = list[i][1]
        elif i in [3,6,9] :
            answer += "R"
            right[0] = list[i][0]
            right[1] = list[i][1]
        else :
            left_dis = abs(left[0] - list[i][0]) + abs(left[1] - list[i][1])
            right_dis = abs(right[0] - list[i][0]) + abs(right[1] - list[i][1])
            if left_dis > right_dis :
                answer += "R"
                right[0] = list[i][0]
                right[1] = list[i][1]
            elif left_dis < right_dis :
                answer += "L"
                left[0] = list[i][0]
                left[1] = list[i][1]
            else :
                if hand == "right" :
                    answer += "R"
                    right[0] = list[i][0]
                    right[1] = list[i][1]
                else :
                    answer += "L"
                    left[0] = list[i][0]
                    left[1] = list[i][1]

    return answer

hand = "left"
a=	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
print(solution(a,hand))