#이코테8

a = input()
summary = 0
data = []
for i in a :
    if i.isdigit() :
        summary += int(i)
    else :
        data.append(i)

data.sort()
print("".join(data)+str(summary))