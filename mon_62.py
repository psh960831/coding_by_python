#이코테 7
a = input()

left_a = a[:int(len(a)/2)]
right_a = a[int(len(a)/2):]
print(left_a)
print(right_a)
left_sum = 0
right_sum = 0
for i in left_a :
    left_sum += int(i)
for i in right_a :
    right_sum += int(i)

if left_sum == right_sum :
    print('LUCKY')
else :
    print('READY')