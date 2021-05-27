# 이코테 6


def solution(food_times, k) :
    now_food = 0
    time = 0
    while time < k :
        if food_times[now_food%len(food_times)] > 0:
            food_times[now_food% len(food_times)] -= 1
            time += 1
            now_food+=1
        else :
            now_food += 1
        print(food_times, now_food)
    if sum(food_times) == 0:
        return -1
    else :
        return (now_food%3)+1


print(solution([3,1,2],5))



