#백준 10809

print(ord('a'))
print(ord('z'))
data = {}
input = "baekjoon"
for i in range(ord('a'),ord('z')+1):
    data[chr(i)] = -1

for i in range(len(input)):
    if data[input[i]] == -1 :
        data[input[i]] = i

print(list(data.values()))