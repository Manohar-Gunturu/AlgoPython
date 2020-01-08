arr = [34, 8, 10, 3, 2, 80, 30, 33, 1]


# max j - i such that a[j] > a[i]
ans = 0
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[j] > arr[i]:
            ans = max(ans, j - 1)

print(ans)