data = [7, 4, 2, 0, 0, 6, 0, 7, 0]
result = 0
for i in range(len(data)):
    count = 0
    for j in data:
        if data[i] <= j:
            count += 1
    if result < len(data) - i - 1 - count:
        result = len(data) - i - 1 - count
print(result)