arr = [5, 4, 3, 2, 1]

for i in range(1, len(arr)):
    j = i - 1
    key = arr[i]
    for j in range(j, -2, -1):
        if j < 0 or key >= arr[j]:
            break
        else:
            arr[j + 1] = arr[j]

    arr[j + 1] = key

print(arr)
