import math
# programmers 2018 카카오 비밀지도
#n	5
#arr1	[9, 20, 28, 18, 11]
#arr2	[30, 1, 21, 17, 28]
#출력	["#####","# # #", "### #", "# ##", "#####"]
def solution(n, arr1, arr2):
    answer = ["#"]*n
    for i in range(0, n):
        answer[i] = str(bin(arr1[i]|arr2[i]))[2:]
        print(answer)
        answer[i] = re.sub('1', '#', '0'*(n-len(answer[i]))+answer[i])
        print(answer)
        answer[i] = re.sub('0', ' ', answer[i])
        print(answer)
    return answer

def solution(n, arr1, arr2):
    answer = []
    add = ""
    for i in range(n) :
        add_list = []
        add_anw = ""
        a = arr1[i]
        b = arr2[i]
        for j in range(n-1,-1,-1) :
            if a>=math.pow(2,j) :
                add_list.append("#")
                a = a-math.pow(2,j)
            else :
                add_list.append(" ")

            if b>=math.pow(2,j) :
                if add_list[-1] == " ":
                    add_list[-1] = "#"
                b= b-math.pow(2,j)

        for k in add_list :
            add_anw+=k

        answer.append(add_anw)

    return answer
arr1=[9, 20, 28, 18, 11]
arr2=[30, 1, 21, 17, 28]
print(solution(5,arr1,arr2))

#출력	["#####","# # #", "### #", "# ##", "#####"]
