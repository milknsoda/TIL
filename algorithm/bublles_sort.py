arr = [55, 7, 78, 12, 42]
# 두 개의 원소를 비교해서 작은건 앞으로, 큰건 뒤로 
n = len(arr)
for k in range(n-1, 0, -1):
    for i in range(k): # n - 1 ~ 1
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

print(arr)