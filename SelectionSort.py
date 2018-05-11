# selection sort and insertion sort difference is well explained at
# https://stackoverflow.com/a/15799095/2717984


arr = [5, 2, 4, 6, 1, 3]
length = len(arr)

for i in range(0, length):
    minimal = i
    for j in range(i, length):
        if arr[j] < arr[minimal]:
            minimal = j
    arr[minimal], arr[i] = arr[i], arr[minimal]

for j in range(0, len(arr)):
    print(arr[j])