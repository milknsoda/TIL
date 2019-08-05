arr = [0, 4, 1, 3, 1, 2, 4, 1]
# 양의 정수, 최대값을 알아야 된다.
# 최대값 = 4
cnt = [0] * 5 # 배열의 인덱스 n - 1 = 4
# 빈도수 계산
for val in arr:
    cnt[val] += 1

# 누적 빈도수 없이 그냥 빈도수만큼 차례대로 넣기
sorted = []
for i in range(len(cnt)):
    for j in range(cnt[i]):
        sorted.append(i)
print(sorted)

# 누적 빈도수 계산
for i in range(1, len(cnt)):
    cnt[i] = cnt[i - 1] + cnt[i]

sort_list = [0] * 8
for k in arr:
    cnt[k] -= 1
    sort_list[cnt[k]] = k

print(sort_list)