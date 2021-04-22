
# 그리디/단속카메라
def solution(routes):
    answer = 0
    routes.sort()
    course = [routes[0]]
    for i in routes :
        left = i[0]
        right = i[1]
        is_in = False
        for now in course :# now[0] = left now[1] = right
            if now[0] <= left and now[1] >= right : # 구간안에있는경우
                now[0] = left
                now[1] = right
                is_in = True
            elif now[0] > left and now[1] >= right : # 오른쪽구간만 겹치는경우
                if right < now[0] : continue
                now[1] = right
                is_in = True
            elif now[0] <= left and now[1] < right : # 왼쪽구간만 겹치는경우
                if left > now[1] : continue
                now[0] = left
                is_in = True
        if not is_in :
            course.append(i)
    print(course)
    answer = len(course)
    return answer

solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]])