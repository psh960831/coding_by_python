a = input()
list = []
num = 0
answer = ""
for i in a :
    if i.isalpha() :
        list.append(i)
    else :
       num = num + int(i)
list.sort()
list.append(str(num))

print("".join(list))
