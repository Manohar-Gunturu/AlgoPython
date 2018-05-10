arr = [5, 2, 4, 6, 1, 3]
for j in range(1, len(arr)):
    key = arr[j]
    i = j - 1
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i = i - 1
    arr[i+1] = key

for j in range(0, len(arr)):
    print(arr[j])

