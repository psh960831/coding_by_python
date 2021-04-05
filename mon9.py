a, b = map(int, input().split())
data = list(map(int, input().split()))
start = 0
end = max(data)
anw = 0
while start<=end :
    sum = 0
    mid = (start+end) // 2
    for i in data :
        if i>mid :
            sum += i - mid
    if sum < b :
        end = mid - 1
    else :
        anw = mid
        start = mid +1

print(anw)