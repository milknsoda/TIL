arr = 'ABC'
n = len(arr)
# for i in range(n): # 중복순열
#     for j in range(n):
#         for k in range(n):
#             print(arr[i], arr[j], arr[k])

for i in range(n):
    for j in range(n):
        if i == j: continue
        for k in range(n):
            if k == i or k == j: continue
            print(arr[i], arr[j], arr[k])